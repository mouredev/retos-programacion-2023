#!/usr/bin/env bash
set -euo pipefail

for i in {1..100}; do
    if ((i % 3 == 0)); then
        ((i % 5 == 0)) && echo "fizzbuzz" || echo "fizz"
        continue
    fi
    ((i % 5 == 0)) && echo "buzz" || echo "${i}"
done
