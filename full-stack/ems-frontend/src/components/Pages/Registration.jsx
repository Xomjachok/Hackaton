import '../../App.css'
import EmployeeComponent from "../EmployeeComponent.jsx";




function Registration() {
    return (
        <>
        <div style={pageStyle}>
            <h1>Registration</h1>
            <p>Create a new account!</p>
            <EmployeeComponent/>
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