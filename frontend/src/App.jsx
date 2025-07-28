import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // State management for chat functionality
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);
  const [styleProfileLoaded, setStyleProfileLoaded] = useState(false);

  // Handle file selection for chat history upload
  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  // Upload chat history file to create style profile
  const handleFileUpload = async () => {
    if (!selectedFile) {
      alert('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:8000/uploadfile/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      if (response.data.style_profile_created) {
        setStyleProfileLoaded(true);
        alert('File uploaded and style profile created successfully!');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file.');
    }
  };

  // Send message to chatbot and get response
  const handleSendMessage = async () => {
    if (!input.trim()) return;
    if (!styleProfileLoaded) {
      alert('Please upload a chat history file first.');
      return;
    }

    const userMessage = { sender: 'user', text: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post('http://localhost:8000/chat/', {
        message: input,
      });
      const botMessage = { sender: 'bot', text: response.data.response };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { sender: 'bot', text: 'Error: Could not get a response.' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }

    setInput('');
  };

  return (
    <div className="App">
      {/* Header section */}
      <div className="header">
        <h1>🦎 ChameleonChatBot</h1>
      </div>
      
      {/* File upload section */}
      <div className="file-upload-container">
        <input type="file" onChange={handleFileChange} accept=".json" />
        <button className="upload-btn" onClick={handleFileUpload}>
          Upload Chat History
        </button>
        {styleProfileLoaded && (
          <span style={{ color: '#4CAF50', fontWeight: 'bold' }}>
            ✓ Style Profile Loaded
          </span>
        )}
      </div>
      
      {/* Chat messages display */}
      <div className="chat-window">
        {messages.length === 0 && (
          <div style={{ 
            textAlign: 'center', 
            color: 'rgba(255, 255, 255, 0.7)', 
            fontSize: '1.1rem',
            marginTop: '2rem'
          }}>
            {styleProfileLoaded 
              ? "Start chatting! I'll mimic the style from your uploaded chat history." 
              : "Upload a chat history JSON file to begin."}
          </div>
        )}
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      
      {/* Message input section */}
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          placeholder="Type a message..."
          disabled={!styleProfileLoaded}
        />
        <button className="send-btn" onClick={handleSendMessage} disabled={!styleProfileLoaded}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
