#!/usr/bin/env python3

"""
Test script to verify a2a_protocol package imports correctly
"""

try:
    from a2a_protocol.pydantic_v2 import (
        Message,
        Part,
        TextPart,
        FilePart,
        DataPart,
        Role,
        TaskState,
        AgentCard
    )
    import a2a_protocol
    print(f"✅ Successfully imported a2a_protocol {a2a_protocol.__version__}")
    
    # Create a simple message to verify functionality
    message = Message(
        role=Role.user,
        parts=[
            Part(root=TextPart(
                type="text",
                text="Hello, agent!",
                metadata={"source": "test"}
            ))
        ],
        metadata={"test": True}
    )
    print(f"✅ Created message object: {message.role}")
    print("✅ Test completed successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}") 