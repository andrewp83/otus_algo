#!/bin/bash

FILE_RES="tmp.out"

function TrapExitHandler() {
    local EXIT_CODE=$?
    rm -f $FILE_RES
    return $EXIT_CODE
}

trap TrapExitHandler EXIT

function PrintUsage() {
    echo "Usage: runtest.sh command test_dir"
}

function Main() {
    local CMD=$1
    local TEST_DIR=$2

    if [[ -z $CMD || -z $TEST_DIR ]]; then
        PrintUsage
        exit 1
    fi

    for FILE_IN in $TEST_DIR/*.in; do
        echo "$FILE_IN"
        $CMD < "$FILE_IN" > "$FILE_RES"
        if [ $? -ne 0 ]; then
           echo "Test $FILE_IN ends with error. Status code: $?"
           exit 1
        fi
        FILE_OUT=${FILE_IN/.in/.out}
        diff -w -u $FILE_RES $FILE_OUT > /dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo "Test $FILE_IN failed:"
            diff -w -U0 $FILE_RES $FILE_OUT
            exit 1
        fi
    done
    echo "Tests OK"
    return 0
}

Main $@
