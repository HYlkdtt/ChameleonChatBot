# ChameleonChatBot CI/CD Testing Strategy

## Test Types

### 1. Unit Tests (`test_main.py`)
- **Mocked API calls** - No real Groq API requests
- **Fast execution** - Runs in CI/CD without secrets
- **Core functionality** - File upload, validation, endpoints

### 2. Integration Tests (`test_api_integration.py`) 
- **Real API calls** - Requires actual Groq API key
- **Skipped in CI/CD** - Only runs locally with real credentials
- **End-to-end testing** - Full workflow validation

## Running Tests

### Local Development (with real API key)
```bash
# Run all tests including integration
export GROQ_API_KEY="your_real_api_key"
pytest tests/ -v

# Run only unit tests (no API calls)
pytest tests/test_main.py -v
```

### CI/CD Pipeline
```bash
# Runs automatically with mocked API
# Only unit tests execute, integration tests are skipped
pytest tests/ -v
```

## CI/CD Benefits
- ✅ Fast execution (no network calls)
- ✅ No secrets required in GitHub Actions
- ✅ Reliable (not dependent on external API)
- ✅ Tests core business logic
- ✅ Catches regressions early

## Local Testing Benefits  
- ✅ End-to-end validation
- ✅ Real API integration testing
- ✅ Performance testing with actual responses
- ✅ API error handling validation
