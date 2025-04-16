.PHONY: generate-models build install-dev clean publish-specs run-examples install-monorepo

# Generate dataclass models from JSON schema
generate-models:
	@echo "Generating models..."
	@./scripts/generate_models.sh

# Build all packages
build: generate-models
	@echo "Building main package..."
	python -m build
	@echo "Building specs package..."
	cd specs && python -m build

# Install development dependencies
install-dev:
	@echo "Installing development dependencies..."
	uv pip install -e .
	uv pip install build datamodel-code-generator pytest

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf dist/ build/ *.egg-info/
	rm -rf specs/dist/ specs/build/ specs/*.egg-info/
	find . -name __pycache__ -type d -exec rm -rf {} +

# Publish specs package to PyPI
publish-specs:
	@echo "Publishing specs package to PyPI..."
	cd specs && python -m build && uv pip install twine && python -m twine upload dist/*

# Run examples
run-examples:
	@echo "Running dataclass example..."
	python examples/dataclass_example.py
	@echo "Running pydantic v2 example..."
	python examples/pydantic_v2_example.py 