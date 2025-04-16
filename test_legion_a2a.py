#!/usr/bin/env python3

"""
Test script to verify legion_a2a and a2a_protocol packages import correctly
"""

try:
    # Test legion_a2a imports
    import legion_a2a
    from legion_a2a.client import A2AClient
    
    print(f"✅ Successfully imported legion_a2a {legion_a2a.__version__}")
    
    # Test a2a_protocol imports
    from a2a_protocol.pydantic_v2 import (
        Message,
        Part,
        TextPart,
        Role
    )
    import a2a_protocol
    print(f"✅ Successfully imported a2a_protocol {a2a_protocol.__version__}")
    
    # Create a client and test functionality
    client = A2AClient(endpoint="https://example.com")
    message = client.create_text_message(
        text="Hello, agent!",
        metadata={"test": True}
    )
    print(f"✅ Created message using client: {message.role}")
    print("✅ Test completed successfully!")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}") 