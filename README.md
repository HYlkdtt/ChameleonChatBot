# Chameleon ChatBot

[![CI/CD Pipeline](https://github.com/HYlkdtt/ChameleonChatBot/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/HYlkdtt/ChameleonChatBot/actions/workflows/ci-cd.yml)

An AI-powered conversational agent that mimics speaking styles based on uploaded chat histories using Groq API and Llama3-8B-8192 model.

⚠️ **Work in Progress**: This project is currently under development. The core functionality is implemented but several features are still being refined and enhanced.

## Current Features

- 🤖 **Basic Style Mimicking**: Analyzes the first message in uploaded chat histories to create simple personality profiles
- 🚀 **Real-time Chat Interface**: Interactive conversation interface with message history display
- 📁 **JSON File Upload**: Basic chat history processing (currently uses first message for style analysis)
- 🔒 **Secure API Integration**: Environment-based Groq API key configuration
- ⚡ **FastAPI Backend**: High-performance async web framework with CORS support

## What's Currently Working

✅ **Backend API**
- File upload endpoint with JSON validation
- Chat endpoint with Groq API integration
- Basic error handling and response formatting
- Environment variable configuration

✅ **Frontend Interface**
- File upload functionality
- Chat message display
- Real-time API communication with axios
- Responsive design with CSS styling

✅ **DevOps**
- GitHub Actions CI/CD pipeline
- Automated testing with pytest
- Code linting and quality checks

## Known Limitations & TODOs

🔄 **Style Analysis** (Currently Basic)
- Only uses the first message for personality profiling
- Needs advanced NLP analysis for better style extraction
- Should analyze multiple messages and conversation patterns

🔄 **Chat Memory** (Not Implemented)
- No conversation context retention between messages
- Each message is processed independently

🔄 **User Experience** (Basic Implementation)
- Simple file upload without drag-and-drop
- Basic error messages without detailed feedback
- No person selection from chat history

🔄 **Testing Coverage** (Partial)
- Basic API endpoint tests implemented
- Missing integration tests with Groq API
- Frontend tests not yet implemented

## Tech Stack

### Backend
- **FastAPI** - Web framework with automatic OpenAPI documentation
- **Groq API** - AI model inference using Llama3-8B-8192
- **Pydantic** - Data validation and type safety
- **Uvicorn** - ASGI server for production deployment
- **python-dotenv** - Environment variable management

### Frontend  
- **React 19** - Modern frontend framework
- **Vite** - Fast build tool and development server
- **Axios** - HTTP client for API requests
- **CSS** - Custom styling for chat interface

### DevOps & Testing
- **GitHub Actions** - Automated CI/CD pipeline
- **Pytest** - Backend testing framework
- **ESLint** - Frontend code quality and linting
- **Git** - Version control with protected main branch

## Quick Start

> **Note**: This is a development version. Some features may not work as expected.

1. **Clone the repository**
   ```bash
   git clone https://github.com/HYlkdtt/ChameleonChatBot.git
   cd ChameleonChatBot
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your Groq API key:
   # GROQ_API_KEY="your_actual_api_key_here"
   ```

4. **Setup Frontend**
   ```bash
   cd ../frontend
   npm install
   ```

5. **Run the Application**
   ```bash
   # Terminal 1: Start Backend
   cd backend
   uvicorn main:app --reload

   # Terminal 2: Start Frontend  
   cd frontend
   npm run dev
   ```

6. **Access the Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## How to Test (Current State)

1. **Upload a Chat History**: Use the sample JSON format below
2. **Start Chatting**: The AI will respond mimicking the style of the first person
3. **Limitations**: Each response is independent, no conversation memory

### Sample Chat Format

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

## Development Status

This project serves as a proof-of-concept for AI-powered style mimicking. The core architecture is solid, but many features need enhancement for production use.

**Current Focus**: Improving style analysis algorithms and adding conversation memory.

## Contributing

Since this is an active development project, contributions are welcome! Please:

1. Check the TODO list above for areas needing work
2. Fork the repository and create a feature branch
3. Test your changes locally
4. Submit a pull request with clear description

## Testing

```bash
# Run backend tests
cd backend
pytest tests/ -v

# Check frontend build
cd frontend  
npm run build
npm run lint
```

## License

MIT License - This is an educational/portfolio project.
