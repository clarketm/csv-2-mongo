#!/usr/bin/env sh

python -m nose2 --start-dir tests --with-coverage --coverage-report "term" --coverage-report "html" $@
