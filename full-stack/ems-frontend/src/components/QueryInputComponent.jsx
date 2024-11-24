import React, { useState } from 'react';
import './QueryInput.css';

const QueryInputComponent = () => {
    const [query, setQuery] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Your input: ${query}`);
        setQuery('');
    };

    return (
        <div className="query-container">
            <form className="query-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    className="query-input"
                    placeholder="Enter your query..."
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                />
                <button type="submit" className="query-button">
                    Send
                </button>
            </form>
        </div>
    );
};

export default QueryInputComponent;
