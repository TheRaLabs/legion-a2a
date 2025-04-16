# A2A Protocol

Python models for Google's [Agent-to-Agent (A2A) Protocol](https://google.github.io/A2A/#/) specification. This package provides both Pydantic and dataclass model implementations, enabling type-safe communication between agents.

Maintained by the team at [Legion AI](https://thelegionai.com/).

## Installation

```bash
pip install a2a-protocol
```

## Usage

### Pydantic v2 Implementation

```python
from a2a_protocol.pydantic_v2 import Message, Part, TextPart, Role

# Create a simple message
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

### Dataclass Implementation

```python
from a2a_protocol.dataclass import Message, TextPart, Role

# Create a simple message using dataclasses
message = Message(
    role=Role.user,
    parts=[
        TextPart(
            type="text",
            text="Hello, agent!",
            metadata={"source": "user_interface"}
        )
    ],
    metadata={"session_id": "12345"}
)
```

## Core Components

### Message Types
- `TextPart`: For text-based messages
- `FilePart`: For file attachments
- `DataPart`: For structured data

### Task Management
- `Task`: Represents a task with its status, history, and artifacts
- `TaskStatus`: Current state of a task (working, completed, failed, etc.)
- `TaskState`: Enum of possible task states

### JSON-RPC Communication
- `JSONRPCRequest`: Standard request format
- `JSONRPCResponse`: Standard response format
- `SendTaskRequest`, `GetTaskRequest`, `CancelTaskRequest`: Specific request types

### Protocol Workflow

```
┌──────────────┐            ┌──────────────┐
│              │            │              │
│   Agent A    │◄──────────►│   Agent B    │
│              │    A2A     │              │
└──────────────┘  Protocol  └──────────────┘
       │                            ▲
       │                            │
       │         ┌──────────┐       │
       └────────►│  Tasks   │◄──────┘
                 │          │
                 └──────────┘
```

## Features

- Full type-checked implementation of the A2A protocol
- Both Pydantic v2 and dataclass implementations
- Complete support for:
  - Task creation and management
  - Messaging between agents
  - File and data transfer
  - Status updates and notifications
  - Error handling

## Protocol Structure

The A2A protocol enables agents to:
1. Create and manage tasks
2. Send and receive messages
3. Share structured data and files
4. Monitor task status and progress
5. Handle errors and notifications

## License

MIT 