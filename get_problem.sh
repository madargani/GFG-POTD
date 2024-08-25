#!/bin/bash
# My First Script

year=${1:-$(TZ='Asia/Kolkata' date +%Y)}
month=${2:-$(TZ='Asia/Kolkata' date +%m)}
day=${3:-$(TZ='Asia/Kolkata' date +%d)}

url="https://practiceapi.geeksforgeeks.org/api/vr/problems-of-day/problems/previous/?year=$year&month=$month"

problem=$(curl "${url}" \
  | jq '.results[]' \
  | jq "select(.date == \"$year-$month-$day 00:00:00\")" \
  | jq '{name: .problem_name, url: .problem_url}')

url=$(echo $problem | jq '.url' | tr -d '"')
name=$(echo $problem | jq '.name' | tr -d '"')

xdg-open "${url}"

path="$year/$month/$day ${name}"

mkdir -p "${path}"
