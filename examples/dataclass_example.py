#!/usr/bin/env python3
"""
Example demonstrating how to use the Agent-to-Agent Protocol with dataclasses.
"""

from datetime import datetime
from a2a_protocol.dataclass import (
    Message,
    TaskStatus,
    TaskState,
    TextPart,
    Task
)

# Create a simple text part
text_part = TextPart(
    type="text",
    text="Hello, how can I help you today?",
    metadata={"timestamp": "2023-06-01T12:00:00Z"}
)

# Create a message from agent to user
message = Message(
    role="agent",
    parts=[text_part],  # In dataclasses, just use the specific part type
    metadata={"agent_id": "assistant-123"}
)

# Create a task status
status = TaskStatus(
    state=TaskState.working,
    message=None,
    timestamp=datetime.now().isoformat()
)

# Create a complete task
task = Task(
    id="task-12345",
    sessionId="session-6789",
    status=status,
    artifacts=[],
    history=[message],
    metadata={"client": "web"}
)

print(f"Task ID: {task.id}")
print(f"Task state: {task.status.state}")
print(f"First message role: {task.history[0].role}")
print(f"First message text: {task.history[0].parts[0].text}") 