#!/usr/bin/env bash
for d in */; do
  rm -rf "${d}.git"*
done
