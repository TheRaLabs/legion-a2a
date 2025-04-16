#!/usr/bin/env python3
"""
Example demonstrating how to use the Agent-to-Agent Protocol with Pydantic v2.
"""

from datetime import datetime
from a2a_protocol.pydantic_v2 import (
    Message,
    Role,
    TaskStatus,
    TaskState,
    TextPart,
    Part,
    Task,
    SendTaskRequest,
    TaskSendParams
)

# Create a simple text part
text_part = TextPart(
    type="text",
    text="Hello, how can I help you today?",
    metadata={"timestamp": "2023-06-01T12:00:00Z"}
)

# Create a Part which is a RootModel that wraps the specific part type
part = Part(root=text_part)

# Create a message from agent to user
message = Message(
    role=Role.agent,
    parts=[part],  # In Pydantic v2, we use the Part wrapper
    metadata={"agent_id": "assistant-123"}
)

# Create a task status
status = TaskStatus(
    state=TaskState.working,
    message=None,
    timestamp=datetime.now()
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

# Create a JSON-RPC request
task_send_params = TaskSendParams(
    id="task-12345",
    message=message
)

request = SendTaskRequest(
    jsonrpc="2.0",
    id="request-123",
    method="tasks/send",
    params=task_send_params
)

# Validate and convert to dictionary
task_dict = task.model_dump()
request_dict = request.model_dump()

print(f"Task ID: {task.id}")
print(f"Task state: {task.status.state.value}")
print(f"First message role: {task.history[0].role.value}")
print(f"First message text: {task.history[0].parts[0].root.text}")
print(f"Request method: {request.method}")
print(f"Request as JSON: {request_dict}") 