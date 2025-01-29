#!/bin/bash

for test_file in test*.py; do
  echo "Running tests in $test_file..."
  python3 -m unittest -v "$test_file"
done