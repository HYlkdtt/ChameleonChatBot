# Chameleon ChatBot

[![CI/CD Pipeline](https://github.com/HYlkdtt/ChameleonChatBot/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/HYlkdtt/ChameleonChatBot/actions/workflows/ci-cd.yml)

An AI-powered conversational agent that mimics speaking styles based on uploaded chat histories using Groq API and Llama3-8B-8192 model.

## Features

- 🤖 **Style Mimicking**: Analyzes chat histories to replicate specific speaking patterns
- 🚀 **Real-time Chat**: Interactive conversation interface with typing indicators
- 📁 **File Upload**: JSON chat history processing and analysis
- 🔒 **Secure API**: Environment-based configuration with Groq API integration
- ⚡ **Fast Performance**: Built with FastAPI and React for optimal speed

## Tech Stack

### Backend
- **FastAPI** - High-performance async web framework
- **Groq API** - AI model inference with Llama3-8B-8192
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server for production deployment

### Frontend  
- **React + Vite** - Modern frontend development
- **Axios** - HTTP client for API communication
- **CSS Grid** - Responsive chat interface design

### DevOps
- **GitHub Actions** - CI/CD pipeline for automated testing
- **Pytest** - Comprehensive backend testing suite
- **ESLint** - Frontend code quality and linting

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/HYlkdtt/ChameleonChatBot.git
   cd ChameleonChatBot
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   # Add your Groq API key to .env
   ```

4. **Setup Frontend**
   ```bash
   cd ../frontend
   npm install
   ```

5. **Run the Application**
   ```bash
   # Terminal 1: Backend
   cd backend
   uvicorn main:app --reload

   # Terminal 2: Frontend  
   cd frontend
   npm run dev
   ```

6. **Access the App**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000

## Usage

1. Upload a JSON chat history file
2. The system analyzes speaking patterns from the first person
3. Start chatting - the AI responds in that person's style!

## Sample Chat Format

```json
[
  {
    "text": "hey what's up! 😊 just chillin here",
    "sender": "john"
  },
  {
    "text": "not much, just working on some code lol", 
    "sender": "sarah"
  }
]
```

## Testing

```bash
# Backend tests
cd backend
pytest tests/ -v

# Frontend linting
cd frontend  
npm run lint
```

## CI/CD Pipeline

The project includes automated GitHub Actions workflows for:
- ✅ Python code linting (flake8)
- ✅ Backend API testing (pytest)
- ✅ Frontend building and linting
- ✅ Artifact generation for deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests locally
5. Submit a pull request

## License

MIT License - see LICENSE file for details.
