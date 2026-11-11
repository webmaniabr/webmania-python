#!/usr/bin/env python3
"""Install actual wheel/sdist into empty venvs and test only installed packages."""
import argparse
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import venv

ROOT=Path(__file__).resolve().parents[1]


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--artifacts',type=Path,required=True)
    p.add_argument('--wheel',type=Path);p.add_argument('--sdist',type=Path)
    p.add_argument('--wheelhouse',type=Path)
    a=p.parse_args();out=a.artifacts.resolve();out.mkdir(parents=True,exist_ok=False)
    environment=os.environ.copy();environment.pop('PYTHONPATH',None);environment.pop('MYPYPATH',None)
    environment['PIP_DISABLE_PIP_VERSION_CHECK']='1'
    if a.wheelhouse:
        environment.update(PIP_NO_INDEX='1',PIP_FIND_LINKS=str(a.wheelhouse.resolve()))
    def command(args,log,cwd=None,expected_returncode=0):
        result=subprocess.run([str(x) for x in args],cwd=cwd or out,env=environment,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (out/log).write_text(result.stdout)
        if result.returncode != expected_returncode:raise SystemExit('Controlled step failed: '+log+' (exit '+str(result.returncode)+')')
        return result.stdout
    if (a.wheel is None)!=(a.sdist is None):raise SystemExit('Provide both candidate wheel and sdist, or neither.')
    if a.wheel is None:
        command([sys.executable,'-m','build','--outdir',out/'dist',ROOT],'build.log')
        wheel=next((out/'dist').glob('*.whl'));sdist=next((out/'dist').glob('*.tar.gz'))
    else:wheel=a.wheel.resolve();sdist=a.sdist.resolve()
    sys.path.insert(0,str(ROOT/'tests'))
    from support import server,send
    try:git=subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],stderr=subprocess.DEVNULL,text=True).strip()
    except (OSError,subprocess.CalledProcessError):git=None
    receipt={'classification':'installed_artifact_controlled_loopback_only','runtime':sys.version,'platform':platform.platform(),'git':git,'artifacts':[]}
    for kind,candidate in [('wheel',wheel),('sdist',sdist)]:
        candidate_hash=digest(candidate)
        directory=out/kind;directory.mkdir();consumer=directory/'empty-consumer';consumer.mkdir()
        venv.create(directory/'venv',with_pip=True,symlinks=os.name!='nt')
        python=directory/'venv'/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        command([python,'-m','pip','install','--constraint',ROOT/'requirements-runtime.lock',candidate],kind+'-install.log',consumer)
        probe=command([python,'-c',"import webmania,importlib.metadata,json,sys; print(json.dumps({'version':webmania.__version__,'module':webmania.__file__,'runtime':sys.version,'distributions':{d.metadata['Name']:d.version for d in importlib.metadata.distributions()}},sort_keys=True))"],kind+'-probe.json',consumer)
        metadata=json.loads(probe)
        if 'site-packages' not in metadata['module'] or str(ROOT/'src') in metadata['module']:raise SystemExit('Source checkout imported instead of installed artifact.')
        def handler(h,r):send(h,{'expiration':30} if 'certificado' in r['path'] else {'status':'online'})
        with server(handler) as (base,records,_):
            command([python,ROOT/'scripts/quickstart.py','--base-url',base],kind+'-quickstart.log',consumer)
            if len(records)!=2:raise SystemExit('Quickstart did not perform exactly two controlled requests.')
        command([python,'-m','unittest','discover','-s',ROOT/'tests','-v'],kind+'-tests.log',consumer)
        command([python,'-m','pip','install','mypy==2.4.0'],kind+'-typing-install.log',consumer)
        command([python,'-m','mypy','--strict','--follow-imports=silent','--no-incremental','--config-file',ROOT/'pyproject.toml',ROOT/'tests/typing_consumer.py',ROOT/'tests/typing_shapes_positive.py'],kind+'-typing.log',consumer)
        negative_file=ROOT/'tests/typing_shapes_negative.py'
        negative=command([python,'-m','mypy','--strict','--follow-imports=silent','--no-incremental','--config-file',ROOT/'pyproject.toml',negative_file],kind+'-typing-negative.log',consumer,expected_returncode=1)
        expected_lines={i for i,line in enumerate(negative_file.read_text().splitlines(),1) if '# expect-error' in line}
        actual_lines={int(n) for n in re.findall(r'typing_shapes_negative\.py:(\d+): error:',negative)}
        if not expected_lines or actual_lines != expected_lines:raise SystemExit('Negative typing cases did not fail at every intended assignment.')
        if digest(candidate)!=candidate_hash:raise SystemExit('Candidate artifact changed during installation.')
        receipt['artifacts'].append({'kind':kind,'name':candidate.name,'sha256':candidate_hash,'installed':metadata,'quickstart_requests':len(records),'suite':'unittest HTTP/TLS loopback, errors, polling, binary, bounds, cancellation','typing':'mypy 2.4.0'})
        print(kind+' installed/quickstart/socket/typing checks passed',flush=True)
    (out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'receipt':str(out/'receipt.json'),'artifacts':[{'kind':x['kind'],'sha256':x['sha256']} for x in receipt['artifacts']]}))


if __name__=='__main__':main()
