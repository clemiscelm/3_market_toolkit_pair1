#!/bin/bash
#
# fetch_prices.sh — validate and summarize the raw price data.
#
# >>> Partner A owns this script. <<<
#
# In a real project this would call an API and download data. Here it inspects
# the local raw data and produces a daily summary log — so you can run one
# command every morning and know what you've got.
#
# Usage:      ./scripts/fetch_prices.sh
# Success:    prints a summary; writes it to logs/fetch_<date>.log; exit 0
# Failure:    prints an error to stderr; exit 1
#
# When done, the following must all be true:
#   - ./scripts/fetch_prices.sh runs green when data/raw/*.csv exists
#   - It creates logs/fetch_YYYY-MM-DD.log with the same content as the console
#   - It exits with code 1 (and prints to stderr) if data/raw/ is missing or empty

# TODO 1: turn on strict mode so any error stops the script immediately.
#         Uncomment the next line:
set -euo pipefail

# TODO 2: set the input directory. Use double quotes.
INPUT_DIR="data/raw"

# TODO 3: set the log directory.
LOG_DIR="logs"

# TODO 4: build the log filename using today's date.
#         HINT:   $(date +%F)   gives you "2026-09-11".
LOG_FILE="$LOG_DIR/fetch_$(date +%F).log"

# TODO 5: make sure the log directory exists.
#         HINT:   mkdir -p "$LOG_DIR"
mkdir -p "$LOG_DIR"

# TODO 6: check that the input directory exists.
#         If not, print an error to stderr (with  >&2) and  exit 1
#         HINT:   if [ ! -d "$INPUT_DIR" ]; then
#                     echo "ERROR: $INPUT_DIR does not exist"  >&2
#                     exit 1
#                 fi
if [ ! -d "$INPUT_DIR" ]; then
	echo "ERROR: $INPUT_DIR does not exist" >&2
	exit 1
fi

# TODO 7: check that at least one .csv file exists in the input directory.
#         If not, error to stderr and exit 1.
#         HINT:  count with:    shopt -s nullglob; files=("$INPUT_DIR"/*.csv); count=${#files[@]}
#         (nullglob makes the glob expand to nothing if no matches, instead of the literal '*')
shopt -s nullglob
files=("$INPUT_DIR"/*.csv)
count=${#files[@]}
if [ "$count" -eq 0 ]; then
	echo "ERROR: no CSV files found in $INPUT_DIR" >&2
	exit 1
fi

# TODO 8: build the summary. Put the whole thing inside a  { ... }  block so
#         you can  tee  it into the log file at the end.
#
#         Inside the block:
#           - print a header line with the date
#           - loop over every  "$INPUT_DIR"/*.csv:
#               - ticker = basename of the file, with .csv removed
#                 HINT:  ticker=$(basename "$f" .csv)
#               - rows = (line count of the file) - 1  (skip the header)
#                 HINT:  rows=$(( $(wc -l < "$f") - 1 ))
#               - echo "  <ticker>: <rows> rows"
#           - print a final line with the total number of files
#
#         Skeleton:
#             {
#                 echo "fetch_prices — $(date +%F)"
#                 echo "input: $INPUT_DIR"
#                 count=0
#                 for f in "$INPUT_DIR"/*.csv; do
#                     ticker=$(basename "$f" .csv)
#                     rows=$(( $(wc -l < "$f") - 1 ))
#                     echo "  $ticker: $rows rows"
#                     count=$((count + 1))
#                 done
#                 echo "total: $count files"
#             } | tee "$LOG_FILE"

echo "fetch_prices.sh — starter. Follow the TODOs above." >&2
exit 1
