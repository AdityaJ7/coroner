#!/usr/bin/env bash

THIS_DIR=$(dirname $(readlink -f $BASH_SOURCE))

export PYTHONPATH=$THIS_DIR/src:$PYTHON_PATH
source venv/bin/activate
