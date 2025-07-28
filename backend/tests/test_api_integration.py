"""
Integration tests that would require real API keys.
These are separated and can be run locally with actual credentials.
"""
import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app
import json
import io

client = TestClient(app)

@pytest.mark.skipif(
    not os.getenv("GROQ_API_KEY") or os.getenv("GROQ_API_KEY") == "fake_api_key_for_testing",
    reason="Real Groq API key not available"
)
def test_real_groq_api_integration():
    """Test with real Groq API - only runs if real API key is available"""
    # Upload a file first
    chat_data = [{"text": "Hello there! How are you doing?", "sender": "john"}]
    json_content = json.dumps(chat_data)
    file_obj = io.BytesIO(json_content.encode())
    
    upload_response = client.post(
        "/uploadfile/",
        files={"file": ("test.json", file_obj, "application/json")}
    )
    assert upload_response.status_code == 200
    
    # Test actual chat with Groq API
    chat_response = client.post(
        "/chat/",
        json={"message": "Hi there!"}
    )
    
    # Should get a real response from Groq
    assert chat_response.status_code == 200
    assert "response" in chat_response.json()
    assert len(chat_response.json()["response"]) > 0
