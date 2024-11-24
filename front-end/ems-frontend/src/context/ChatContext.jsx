import React, { createContext, useState, useContext } from "react";

const ChatContext = createContext();

export const useChatContext = () => useContext(ChatContext);

export const ChatProvider = ({ children }) => {
    const [chats, setChats] = useState([]);
    const [isSidebarVisible, setSidebarVisible] = useState(true);

    const addNewChat = () => {
        const newChat = { id: Date.now(), title: `Chat ${chats.length + 1}`, active: false };
        setChats([...chats, newChat]);
    };

    const toggleSidebar = () => setSidebarVisible(!isSidebarVisible);

    return (
        <ChatContext.Provider value={{ chats, setChats, isSidebarVisible, toggleSidebar, addNewChat }}>
            {children}
        </ChatContext.Provider>
    );
};
