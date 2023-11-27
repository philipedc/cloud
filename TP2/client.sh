#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <song1> <song2> <song3> ..."
    exit 1
fi

# Convert arguments to JSON array
songs=()
for song in "$@"; do
    songs+=("\"$song\"")
done

# Join array elements with commas to create a JSON array
songs_json="[ $(IFS=,; echo "${songs[*]}") ]"

# Make the wget call
wget --server-response \
     --output-document response.out \
     --header='Content-Type: application/json' \
     --post-data "{\"songs\": $songs_json}" \
     http://10.102.65.18:32211/api/recommend
