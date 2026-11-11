#!/bin/sh
# Exemplo neutro de homologação: roda o SDK deste checkout (dependências já instaladas).
# Sem WEBMANIA_LIVE=1 o exemplo não faz requisições e sai com 77.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$here/../.." && pwd)
PYTHONPATH="$root/src${PYTHONPATH:+:$PYTHONPATH}" PYTHONDONTWRITEBYTECODE=1 exec python3 "$here/main.py"
