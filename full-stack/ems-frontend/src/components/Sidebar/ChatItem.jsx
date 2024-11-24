import React from "react";

const ChatItem = ({ chat, onClick }) => {
    return (
        <li
            className={`chat-item ${chat.active ? "active" : ""}`}
            onClick={onClick}
            role="button"
            tabIndex={0}
        >
            {chat.title}
        </li>
    );
};

export default ChatItem;
