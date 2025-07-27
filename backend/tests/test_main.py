import pytest
from fastapi.testclient import TestClient
from backend.main import app
import json
import io

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns correct message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ChameleonChatBot backend is running!"}

def test_upload_valid_json():
    """Test uploading a valid JSON chat history file"""
    # Create a mock JSON file
    chat_data = [
        {"text": "Hello there!", "sender": "john"},
        {"text": "Hi! How are you?", "sender": "sarah"}
    ]
    
    # Convert to file-like object
    json_content = json.dumps(chat_data)
    file_obj = io.BytesIO(json_content.encode())
    
    response = client.post(
        "/uploadfile/",
        files={"file": ("test.json", file_obj, "application/json")}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test.json"
    assert data["style_profile_created"] == True

def test_upload_invalid_file():
    """Test uploading a non-JSON file"""
    file_obj = io.BytesIO(b"This is not JSON")
    
    response = client.post(
        "/uploadfile/",
        files={"file": ("test.txt", file_obj, "text/plain")}
    )
    
    assert response.status_code == 400
    assert "Invalid file type" in response.json()["detail"]

def test_chat_without_upload():
    """Test chatting without uploading a file first"""
    response = client.post(
        "/chat/",
        json={"message": "Hello"}
    )
    
    assert response.status_code == 400
    assert "No style profile loaded" in response.json()["detail"]

def test_upload_invalid_json():
    """Test uploading a file with invalid JSON"""
    file_obj = io.BytesIO(b'{"invalid": json content}')
    
    response = client.post(
        "/uploadfile/",
        files={"file": ("invalid.json", file_obj, "application/json")}
    )
    
    assert response.status_code == 400
    assert "Invalid JSON file" in response.json()["detail"]
