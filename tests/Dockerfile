ARG PYTHON_IMAGE=python:3.11-slim@sha256:b7a9e5f6a93d6d4a31f129bbd4bdee69efccb6ded0fb230d78aafaf37af98377
FROM ${PYTHON_IMAGE}
RUN apt-get update && apt-get install -y --no-install-recommends openssl && rm -rf /var/lib/apt/lists/*
WORKDIR /sdk-harness
COPY requirements-runtime.lock requirements-dev.lock pyproject.toml ./
RUN python -m pip download --only-binary=:all: -r requirements-dev.lock -d /wheels
COPY tests ./tests
COPY scripts ./scripts
COPY examples ./examples
COPY dist ./dist
RUN python -c "import hashlib,json,pathlib,platform,sys; print(json.dumps({'runtime':sys.version,'platform':platform.platform(),'wheels':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in pathlib.Path('/wheels').iterdir()}},sort_keys=True))" > /runtime-and-wheel-hashes.json
CMD ["python", "scripts/test_installed.py", "--artifacts", "/tmp/installed-artifacts", "--wheel", "/sdk-harness/dist/webmania_sdk-0.1.0a8-py3-none-any.whl", "--sdist", "/sdk-harness/dist/webmania_sdk-0.1.0a8.tar.gz", "--wheelhouse", "/wheels"]
