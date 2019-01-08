#!/usr/bin/env bash

PACKAGE_NAME="doob_boot"

with_rednose="--rednose --force-color"
# with_coverage="--cover-html-dir=${BASE_DIR}/htmlcov --with-coverage --cover-html --cover-package=${PACKAGE_NAME} --cover-erase --cover-branches"
# with_doctest="--with-doctest"


nosetests ${with_rednose} -s -v -w tests 