#!/usr/bin/env bash

THIS_DIR=$(dirname $(readlink -f $BASH_SOURCE))

export PYTHONPATH=$THIS_DIR:$PYTHON_PATH
source venv/bin/activate
