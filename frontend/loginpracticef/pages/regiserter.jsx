import { useState } from "react";

function Register(){

    const [username,setusername] = useState();
    const [email,setEmail] = useState();
    const [phone_number,setphone_number] = useState();
    const [password,setpassword] = useState();
    

    return(
        <>
            <form action="">
                <h2>Register</h2>
                <label htmlFor="name">Username : </label> 
                <input type="text" id="name" name="name" value={username}/> 
                <label htmlFor="email">email : </label>
                <input type="email" id="email" name="email" value={email}/>
                <label htmlFor="phone_number">Phone_number :</label>
                <input type="number" name="phone_number" id="phone_number" step="1" min="0" value={phone_number}/>
                <label htmlFor="password">Password : </label>
                <input type="password" name="password" id="password" value={password} />
            </form>
        </>
    );
}

export default Register;
