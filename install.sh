#!/bin/bash
set -eu
remove=
if [[ ${1:-} == "--remove" ]]; then
    remove=1
fi
mkdir -p "${HOME}/.cookiecutters"
SCRIPT_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

for directory in "${SCRIPT_DIR}/"*/; do
    symlink="${HOME}/.cookiecutters/ns-$(basename "${directory}")"
    rm -f "${symlink}"
    if [[ -z ${remove} ]]; then
        ln -sf "${directory}" "${symlink}"
    fi
done
