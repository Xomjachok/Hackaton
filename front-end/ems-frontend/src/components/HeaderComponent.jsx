import React from 'react';
import logo from '../assets/logo.png';
import './Header.css';

const HeaderComponent = () => {
    return (
        <div>
            <header>
                <nav className="navbar navbar-dark bg-dark d-flex align-items-center justify-content-between" style={{ padding: '1%' }}>
                    {/* Логотип */}
                    <div className="d-flex align-items-center">
                        <img className="header-logo" src={logo} alt="Logo" style={{ marginRight: '10%' }} />
                        <h1 className="navbar-brand mb-0">Non-Stop Energy</h1>
                    </div>
                    {/* Аватар користувача */}
                    <div className="user-avatar">
                        <div
                            style={{
                                width: '40px',
                                height: '40px',
                                backgroundColor: '#ffffff',
                                borderRadius: '50%',
                                display: 'flex',
                                justifyContent: 'center',
                                alignItems: 'center',
                                color: '#000',
                            }}
                        >
                            U
                        </div>
                    </div>
                </nav>
            </header>
        </div>
    );
};

export default HeaderComponent;
