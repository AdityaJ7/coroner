#!/usr/bin/env bash

THIS_DIR=$(dirname $(readlink -f $BASH_SOURCE))
pushd $THIS_DIR

export PYTHONPATH=$THIS_DIR/src:$PYTHON_PATH
source venv/bin/activate

echo -e "\033[32mSetup Complete\033[0m"
