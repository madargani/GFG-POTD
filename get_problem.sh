#!/bin/bash
# My First Script

url="https://practiceapi.geeksforgeeks.org/api/vr/problems-of-day/problems/previous/?year=2024&month=8"

date=${1:-$(TZ='Asia/Kolkata' date +%F)}

problem=$(curl "${url}" \
  | jq '.results[]' \
  | jq "select(.date == \"$date 00:00:00\")" \
  | jq '{name: .problem_name, url: .problem_url}')

xdg-open $(echo $problem | jq '.url' | tr -d '"')

mkdir "$PWD/$(sed 's|-|/|g' <<< $date) $(echo $problem | jq '.name' | tr -d '"')/"
