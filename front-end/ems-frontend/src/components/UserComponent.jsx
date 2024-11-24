import React, { useState } from 'react';
import './Pages/Registration.css'

const UserComponent = () => {
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        const user = { login, password, email };
        console.log(user);
    };

    return (

        <div >
            <div className="input-container">



                <div >

                    <form onSubmit={handleSubmit} className="form">
                        <div className="input-container">
                            <label>Login</label>
                            <input
                                type="text"
                                placeholder="Create a login"
                                className="form-control"
                                value={login}
                                onChange={(e) => setLogin(e.target.value)}
                            />
                        </div>
                        <div className="input-container">
                            <label>Password</label>
                            <input
                                type="text"
                                placeholder="Сreate a password"
                                className="form-control"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>
                        <div className="input-container">
                            <label>Email</label>
                            <input
                                type="email"
                                placeholder="Enter email"
                                className="form-control"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </div>
                        <h1></h1>
                        <button type="submit" className="btn btn-primary align-content-center align-content-between sendButton">
                            Create Account
                        </button>
                    </form>

                </div>
            </div>
        </div>
    );
};

export default UserComponent