#!/usr/bin/env bash

coverage run --source doob_bot -m pytest tests -p no:warnings
coverage report