import pytest
from fastapi.testclient import TestClient
import sys
import os

# Set fake API key to avoid Groq client initialization error
os.environ["GROQ_API_KEY"] = "fake_api_key_for_testing"

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns correct message"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ChameleonChatBot backend is running!"}

def test_app_startup():
    """Test that the FastAPI app can start without errors"""
    assert app is not None
    assert hasattr(app, 'routes')
    assert len(app.routes) > 0

def test_endpoints_exist():
    """Test that required endpoints are available"""
    # Upload endpoint should exist
    response = client.post("/uploadfile/")
    assert response.status_code == 422
    
    # Chat endpoint should exist  
    response = client.post("/chat/")
    assert response.status_code == 422
