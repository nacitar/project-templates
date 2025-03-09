#!/bin/bash
set -eu
remove=
if [[ ${1:-} == "--remove" ]]; then
    remove=1
fi
mkdir -p "${HOME}/.cookiecutters"
SCRIPT_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"

for directory in "${SCRIPT_DIR}/"*/; do
    name=$(basename "${directory}")
    if [[ ${name} == "SHARED" ]]; then
        continue
    fi

    symlink="${HOME}/.cookiecutters/ns_${name}"

    rm -f "${symlink}"
    if [[ -z ${remove} ]]; then
        ln -sf "${directory}" "${symlink}"
    fi
done
