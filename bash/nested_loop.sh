#!/bin/bash

arr=(50 100 150 200)  # Define an array with your values

for i in "${arr[@]}"
do
  for j in {1..3}
  do
    echo "i:$i, j:$j"
  done
done
