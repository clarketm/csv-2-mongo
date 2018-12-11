#!/usr/bin/env sh

rm -rf ./build/ ./*'.egg-info'/ ./dist/
python setup.py sdist bdist_wheel
