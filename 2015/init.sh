#!/usr/bin/env bash

ADVENT_OF_CODE_URL=https://adventofcode.com
YEAR=2015
INPUTS_DIR=inputs
DAYS_DIR=src/days
DAYS=$(seq 1 25)
ENV_FILE=.env
EXT=py
TEMPLATE=day.template.txt


fetch_inputs() {
    echo "Fetching inputs from $ADVENT_OF_CODE_URL to $INPUTS_DIR/"
    echo

    mkdir -p ${INPUTS_DIR}

    source $ENV_FILE 2>/dev/null

    if [ -z $AOC_COOKIE ]; then
        echo "${FUNCNAME[0]}: error: AOC_COOKIE must be set in order to fetch inputs, either in $ENV_FILE or as environment variable" >&2
        exit
    fi

    for day in $DAYS; do
        echo -n "input $day --> "

        path="$INPUTS_DIR/input$day.txt"
        url="$ADVENT_OF_CODE_URL/$YEAR/day/$day/input"

        if [ -f $path ]; then
            echo EXISTS
            continue
        fi

        response=$(curl -s --cookie "session=$AOC_COOKIE" -w "%{http_code}" "$url")
        status=${response: -3}

        if [ $status -ne 200 ]; then
            echo "FAIL: request to $url failed with status $status"
            continue
        fi

        input=${response:0:${#response}-3}

        if [ $? -eq 0 ]; then
            # Remove trailing newline if present
            input=${input%$'\n'}
            echo -n "$input" > $path
            echo OK
        else
            echo FAIL
        fi
    done
}

create_days() {
    echo "Creating day templates in $DAYS_DIR/"
    echo

    mkdir -p ${DAYS_DIR}

    if [ ! -f $TEMPLATE ]; then
        echo "${FUNCNAME[0]}: error: template file $TEMPLATE not found" >&2
        exit
    fi

    for day in $DAYS; do
        echo -n "day $day --> "

        path="$DAYS_DIR/day$day.$EXT"

        if [ -f $path ]; then
            echo "EXISTS"
            continue
        fi

        cp $TEMPLATE $path 2>/dev/null && echo OK || echo FAIL        
    done
}

fetch_inputs
echo
echo
create_days
