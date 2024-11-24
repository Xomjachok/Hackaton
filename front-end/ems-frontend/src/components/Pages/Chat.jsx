import '../../App.css';
import QueryInputComponent from "../QueryInputComponent.jsx";
import Sidebar from "../Sidebar/Sidebar";
import { ChatProvider } from "../../context/ChatContext";
import HeaderComponent from "../HeaderComponent.jsx";
import FooterComponent from "../FooterComponent.jsx";
import './Chat.css';
import React, { useState } from "react";

function Chat() {
    const [file, setFile] = useState(null); // State for file upload
    const [prompt, setPrompt] = useState(''); // State for user query
    const [chatHistory, setChatHistory] = useState([]); // State for chat history

    const uploadFile = async () => {
        if (!file) {
            alert('Please select a file!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);
        formData.append('prompt', prompt);

        const response = await fetch('http://localhost:5000/generate-chart', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();
        if (data.chart_data) {
            return JSON.parse(data.chart_data);
        } else {
            console.error(data.error);
            return null;
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await uploadFile();
        if (response) {
            // Add user query and AI response to chat history
            setChatHistory((prevHistory) => [
                ...prevHistory,
                { user: prompt, bot: response }
            ]);
        }
        setPrompt(''); // Clear the input field after submission
    };

    return (
        <>
            {/* Header */}
            <HeaderComponent />

            {/* Chat Context Provider */}
            <ChatProvider>
                <div className="app">
                    {/* Sidebar */}
                    <Sidebar />

                    {/* Main Content */}
                    <div className="chat-main-content">
                        {/* Chat History */}
                        <div className="chat-history">
                            {chatHistory.map((entry, index) => (
                                <div key={index} className="chat-entry">
                                    <div className="user-message">
                                        <strong>You:</strong> {entry.user}
                                    </div>
                                    <div className="bot-response">
                                        <strong>AI:</strong>
                                        <pre>{JSON.stringify(entry.bot, null, 2)}</pre>
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/* File Upload and Query Form */}
                        <form onSubmit={handleSubmit} className="file-query-form">
                            {/* File Input */}
                            <input
                                type="file"
                                onChange={(e) => setFile(e.target.files[0])}
                                className="file-input"
                            />

                            {/* Query Input */}
                            <textarea
                                className="query-input"
                                placeholder="Enter your query..."
                                value={prompt}
                                onChange={(e) => setPrompt(e.target.value)}
                            />

                            {/* Submit Button */}
                            <button type="submit" className="generate-button">
                                Submit
                            </button>
                        </form>
                    </div>
                </div>
            </ChatProvider>

            {/* Footer */}
            <FooterComponent />
        </>
    );
}

export default Chat;
