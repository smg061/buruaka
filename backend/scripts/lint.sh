#!/usr/bin/env bash

set -x

mypy src
black src --check
isort  src
flake8
