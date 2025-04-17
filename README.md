# Legion A2A

Legion A2A is an implementation of the Agent to Agent Protocol, providing tools and utilities for building agent-to-agent communications.

## Project Structure

This is a monorepo containing:

- `a2a-protocol`: Core protocol models and specifications (in `a2a_protocol/`)

For detailed information about the protocol, please see the [a2a_protocol/README.md](a2a_protocol/README.md).

## Installation

```bash
# Or install just the protocol models
pip install a2a-protocol
```

## Usage

```python
# Work directly with the protocol models
from a2a_protocol.pydantic_v2 import Message, Part, TextPart, Role

# Create a message
message = Message(
    role=Role.user,
    parts=[
        Part(root=TextPart(
            type="text",
            text="Hello, agent!",
            metadata={"source": "user_interface"}
        ))
    ],
    metadata={"session_id": "12345"}
)
```

## Development

This project uses PEP 625 compliant build configuration with `pyproject.toml`.

### Setup

```bash
# Clone the repository
git clone https://github.com/TheRaLabs/legion-a2a.git
cd legion-a2a

# Install in development mode
pip install -e .
```

## Publishing to PyPI

To publish the a2a-protocol package to PyPI:

```bash
# Navigate to the protocol directory
cd a2a_protocol

# Remove old build and build the package
rm -rf dist build && python -m build

# Upload to PyPI
python -m twine upload dist/*
```

Make sure you have the required dependencies installed:
```bash
pip install build twine
```

## License

MIT