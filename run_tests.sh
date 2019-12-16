#!/usr/bin/env bash

TRAVIS_BRANCH=master

FILES=$(git diff --name-only --diff-filter=AM ${TRAVIS_BRANCH}...HEAD | grep "\.py$" | sort)

for x in $FILES; do
    python ${x}
done
