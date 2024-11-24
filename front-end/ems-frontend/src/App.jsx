import './App.css'
// import ListEmployeeComponent from './components/ListEmployeeComponent';

import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Chat from "./components/Pages/Chat.jsx";
import Home from "./components/Pages/Home.jsx";
import Login from "./components/Pages/Login.jsx";
import Registration from "./components/Pages/Registration.jsx";


function App() {

  return (
      <>
        <BrowserRouter>

          <Routes>
            {/* // http://localhost:3000 */}
            <Route path='/' element = { <Home/> }> </Route>

            {/* // http://localhost:3000/login */}
            <Route path='/login' element = { <Login/> } > </Route>

            {/* // http://localhost:3000/registration */}
            <Route path='/registration' element = { <Registration/> }> </Route>

            {/* // http://localhost:3000/chat */}
            <Route path='/chat' element = { <Chat/> }> </Route>
          </Routes>

        </BrowserRouter>
      </>
  )
}

export default App

