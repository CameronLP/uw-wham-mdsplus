#!/bin/bash
set -e

#. /usr/local/mdsplus/setup.sh


if [[ "x$default_tree_path" == "x" ]]; then
    export default_tree_path="/trees/~t/"
fi

# Everything realted 
mkdir -p /my_tree
export my_tree_path=/my_tree

$@
