#!/bin/bash

echo "Cleanup after python build tests locally"


rm -rf ./__pycache__
rm -rf ./src/app/api/__pycache__/
rm -rf ./src/app/__pycache__/
rm -rf ./src/tests/__pycache__/

echo "Cleaned"
