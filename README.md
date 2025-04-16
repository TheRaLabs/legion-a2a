# Legion A2A

Legion A2A is an implementation of the Agent to Agent Protocol, providing tools and utilities for building agent-to-agent communications.

## Project Structure

This is a monorepo containing:

- `a2a-protocol`: Core protocol models and specifications (in `a2a_protocol/`)
- `legion-a2a`: High-level client implementations and utilities

## Installation

```bash
# Install the main package (includes the a2a-protocol dependency)
pip install legion-a2a

# Or install just the protocol models
pip install a2a-protocol
```

## Usage

```python
from legion_a2a.client import A2AClient

# Create a client
client = A2AClient(endpoint="https://your-a2a-endpoint.com", api_key="your-api-key")

# Create a simple text message
message = client.create_text_message(
    text="Hello, agent!",
    metadata={"session_id": "12345"}
)

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

## License

MIT