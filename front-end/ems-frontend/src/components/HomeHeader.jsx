import logo from '../assets/logo.png';

import './HomeHeader.css';
const HeaderComponent = () => {
    return (
        <div>
            <header>
                <nav className="navbar navbar-dark  d-flex align-items-center justify-content-between"
                     style={{padding: '1%'}}>

                    <div className="d-flex align-items-center">
                        <img className="header-logo" src={logo} alt="Logo" style={{marginRight: '10%'}}/>
                        <h1 className="navbar-brand mb-0">Non-Stop Energy HOME</h1>
                    </div>



                    <nav>
                        <ul className="nav-list">
                            <li className="nav-item ">
                                <a href="/Login">Log In</a>
                            </li>
                        </ul>
                    </nav>

                </nav>
            </header>
        </div>
    );
};

export default HeaderComponent;
