#!/usr/bin/env bash

python3 -m coverage run --source doob_bot -m pytest tests -p no:warnings
python3 -m coverage report