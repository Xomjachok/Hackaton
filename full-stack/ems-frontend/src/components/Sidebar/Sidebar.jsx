import React from "react";
import { useChatContext } from "../../context/ChatContext";
import ChatList from "./ChatList";
import "./Sidebar.css";

const Sidebar = () => {
    const { isSidebarVisible, toggleSidebar, addNewChat } = useChatContext();

    return (
        <div className={`sidebar-container`}>
            {/* Sidebar Content */}
            <div className={`sidebar ${isSidebarVisible ? "visible" : "hidden"}`}>
                <div className="top-bar">
                    <button onClick={addNewChat} aria-label="Add New Chat">➕</button>
                </div>
                {isSidebarVisible && <ChatList />}
            </div>

            {/* Persistent Toggle Button */}
            <button
                className={`toggle-btn ${isSidebarVisible ? "open" : "closed"}`}
                onClick={toggleSidebar}
                aria-label="Toggle Sidebar"
            >
                {isSidebarVisible ? "⬅️" : "➡️"}
            </button>
        </div>
    );
};

export default Sidebar;
