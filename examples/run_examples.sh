#!/bin/bash
set -e

echo "Running dataclass example..."
python -m examples.dataclass_example

echo
echo "Running pydantic v2 example..."
python -m examples.pydantic_v2_example 