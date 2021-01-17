#!/bin/bash

git checkout find-bug
git bisect start
git bisect bad
git bisect good 1.0
git bisect run sh -c "openssl enc -base64 -A -d < home-screen-text.txt | grep -v jackass"

