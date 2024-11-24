import '../../App.css'
import QueryInputComponent from "../QueryInputComponent.jsx";
import Sidebar from "../Sidebar/Sidebar";
import { ChatProvider } from "../../context/ChatContext";
import HeaderComponent from "../HeaderComponent.jsx";
import FooterComponent from "../FooterComponent.jsx";
function Chat() {

    return (
        <>
            <HeaderComponent />



                <ChatProvider>
                    <div className="app">

                        <Sidebar />

                    </div>
                </ChatProvider>

                <QueryInputComponent/>

            <FooterComponent />

        </>
    )
}

export default Chat
