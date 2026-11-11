# Testes e desenvolvimento

Como compilar e testar o SDK para Python a partir da fonte. O contrato fixado e a versão estão descritos em [INTEGRATION.md](INTEGRATION.md).

O fluxo usado pelo workflow do repositório constrói wheel e sdist e roda a suíte em consumidores vazios:

```sh
python -m pip install -r requirements-dev.lock
python scripts/test_installed.py --artifacts artifacts/local
```

A suíte (`unittest`) usa fixtures HTTP/TLS loopback e não faz chamadas fiscais reais.
