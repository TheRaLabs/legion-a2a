#!/bin/bash
set -e

# Create directories if they don't exist
mkdir -p a2a_protocol/dataclass

echo "Generating dataclass models..."
# Generate dataclass models
datamodel-codegen \
  --input a2a_protocol/original/a2a.json \
  --input-file-type jsonschema \
  --output a2a_protocol/dataclass/__init__.py \
  --output-model-type dataclasses.dataclass \
  --disable-timestamp

echo "Models successfully generated!"

# Note: Pydantic v2 models are manually defined in a2a_protocol/pydantic_v2/__init__.py 