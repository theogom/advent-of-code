#!/usr/bin/env bash

# Bash script to fetch inputs, create day templates and run days for Advent of Code
# https://adventofcode.com

# Constants

ADVENT_OF_CODE_URL=https://adventofcode.com
INPUTS_DIR=inputs
DAYS_DIR=src/days
ENV_FILE=.env
TEMPLATE=day.template
YEARS=(2015 2022)
declare -A LANGUAGES=([2015]="python" [2022]="typescript")
declare -A EXTENSIONS=(["python"]="py" ["typescript"]="ts")

# Colors

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

# Messages functions

usage() {
    echo 'usage: ./aoc.sh -y <2015-2022> -d <1-25> -c <init|run>'
}

error() {
    echo -e "${RED}[x] $@${NC}" >&2
}

warn() {
    echo -e "${YELLOW}[!] $@${NC}"
}

success() {
    echo -e "${GREEN}[+] $@${NC}"
}

info() {
    echo -e "[*] $@"
}

# Parse options

OPTS=$(getopt d:y:c:h $*)

if [ $? -ne 0 ]; then
    exit 2
fi

set -- $OPTS
while :; do
    case "$1" in
    -y)
        year=$2
        shift 2
        ;;
    -d)
        day=$2
        shift 2
        ;;
    -c)
        command=$2
        shift 2
        ;;
    -h)
        usage
        exit 0
        ;;
    --)
        shift
        break
        ;;
    esac
done

if [[ -z $year || -z $day || -z $command ]]; then
    usage
    exit 1
fi

if [[ $year -lt 2015 || $year -gt 2022 ]]; then
    error "year must be between 2015 and 2022"
    usage
    exit 1
fi

if [[ $day -lt 1 || $day -gt 25 ]]; then
    error "day must be between 1 and 25"
    usage
    exit 1
fi

if [[ $command != "init" && $command != "run" ]]; then
    error "command must be either init or run"
    usage
    exit 1
fi

if [[ ! " ${YEARS[@]} " =~ " ${year} " ]]; then
    warn "year $year not configured yet"
    exit 1
fi

language=${LANGUAGES[$year]}
ext=${EXTENSIONS[$language]}

# Functions

fetch_input() {
    info "fetching input"

    inputs_path=$year/$INPUTS_DIR
    mkdir -p $inputs_path
    path="$inputs_path/input$day.txt"
    url="$ADVENT_OF_CODE_URL/$year/day/$day/input"

    source $ENV_FILE 2>/dev/null

    if [ -z $AOC_COOKIE ]; then
        error "AOC_COOKIE must be set in order to fetch inputs, either in $ENV_FILE or as environment variable"
        return
    fi

    response=$(curl -s --cookie "session=$AOC_COOKIE" -w "%{http_code}" "$url")
    status=${response: -3}

    if [ $status -ne 200 ]; then
        error "request to $url failed with status $status"
        return
    fi

    input=${response:0:${#response}-3}

    if [ $? -eq 0 ]; then
        # Remove trailing newline if present
        input=${input%$'\n'}
        echo -n "$input" >$path
        success "input $day fetched"
    else
        error "failed to fetch input $day"
    fi
}

create_template() {
    info "creating day template"

    days_path=$year/$DAYS_DIR
    template_path=$year/$TEMPLATE.$ext.txt
    mkdir -p $days_path

    if [ ! -f $template_path ]; then
        error "template file $template_path not found"
        return
    fi

    path="$days_path/day$day.$ext"

    if [ -f $path ]; then
        warn "day $day already exists"
        return
    fi

    cp $template_path $path 2>/dev/null && success "day $day created" || error "failed to create day $day"
}

# Run all days
run_days() {
    info "running days"
    echo
    echo "=== 🎄Advent of Code🎄 ==="
    echo "Link: https://adventofcode.com"
    echo

    for year in "${YEARS[@]}"; do
        make -C $year
    done
}

# Run all days for given year
run_days_by_year() {
    info "running days for year $year"
    echo
    echo "=== 🎄Advent of Code $year🎄 ==="
    echo "Link: https://adventofcode.com/$year"
    echo

    make -C $year
}

# Run day for given day and year
run_day() {
    info "running day"
    echo
    echo "=== 🎄Advent of Code $year🎄 ==="
    echo "Link: https://adventofcode.com/$year/day/$day"
    echo

    make -C $year day$day
}

# Infos

info "year: $year"
info "day: $day"
info "language: ${LANGUAGES[$year]}"
echo

# Execution

case $command in
init)
    fetch_input
    echo
    create_template
    ;;
run)
    run_day
    ;;
esac
