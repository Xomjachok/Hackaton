import '../../App.css'
import './Registration.css'
import UserComponent from "../UserComponent.jsx";
import logo from "../../assets/logo.png";
import React from "react";




function Registration() {
    return (
        <>

            <div style={pageStyle}>
                <div className="logo-container">
                    <img
                        src={logo}
                        alt="Logo"
                        className="logos"
                        style={{marginRight: '10%'}}
                    />
                </div>
                <h1 className="form-heading">Registration</h1>
                <p className="form-heading">Create a new account!</p>
                <h1></h1>

                <UserComponent/>

            </div>


        </>
    );
}

const pageStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f9f9f9',
    color: '#333',
};

export default Registration