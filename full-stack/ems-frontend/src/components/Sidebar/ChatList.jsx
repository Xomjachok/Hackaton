import React from "react";
import { useChatContext } from "../../context/ChatContext";
import ChatItem from "./ChatItem";

const ChatList = () => {
    const { chats, setChats } = useChatContext();

    const handleChatClick = (id) => {
        setChats(chats.map(chat => ({ ...chat, active: chat.id === id })));
    };

    return (
        <ul className="chat-list">
            {chats.map((chat) => (
                <ChatItem key={chat.id} chat={chat} onClick={() => handleChatClick(chat.id)} />
            ))}
        </ul>
    );
};

export default ChatList;
