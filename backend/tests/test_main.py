import pytest
from fastapi.testclient import TestClient
import sys
import os
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
    # Check upload endpoint exists (even if it fails without proper data)
    response = client.post("/uploadfile/")
    # Should return 422 (validation error) not 404 (not found)
    assert response.status_code == 422
    
    # Check chat endpoint exists (even if it fails without proper data)
    response = client.post("/chat/")
    # Should return 422 (validation error) not 404 (not found)  
    assert response.status_code == 422
