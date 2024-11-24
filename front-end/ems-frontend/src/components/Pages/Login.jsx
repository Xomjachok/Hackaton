import './Login.css'
import colorcolor from '../../assets/colorcolor.png';
function Login() {
    return (
<>
    <div className="form-container">
        <div className="logo-container">
            <img
                src={colorcolor}
                alt="Logo"
                className="logos"
                style={{marginRight: '15%'}}
            />
        </div>
        <form className="form">
            <h2 className="form-heading">Log In</h2>
            <div className="input-container">
                <input
                    type="text"
                    placeholder="Username or Email"
                    className="input"
                />
                <input
                    type="password"
                    placeholder="Password"
                    className="input"
                />
            </div>
            <button type="submit" className="submit-button">
                Log In
            </button>
            <p className="signup-text">
                Don’t have an account?{' '}
                <a href="/Registration" className="signup-link">
                    Sign Up
                </a>
            </p>
        </form>

    </div>
</>
    );
}


export default Login
