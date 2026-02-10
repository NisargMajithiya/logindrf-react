import './loginform.css';
import { useState } from "react";
import { useAuth } from "../context/authcontext";
import { useNavigate } from "react-router-dom";

function Loginform(){

   const { login } = useAuth();       // <-- move inside component
   const navigate = useNavigate();    // <-- move inside component

   const [username,setEmail] = useState("");
   const [password,setpassword] = useState("");

   const handleSubmit = async (e) =>{
      e.preventDefault();

      if(!username || !password){
         alert("username and password required");
         return;
      }

      const success = await login(username,password);

      if(success){
         navigate("/dashboard");

         
      } else {
         alert("Invalid credentials");
      }
   }

   return (
     <div className="form-wrapper">     {/* <-- animation wrapper */}
       <form onSubmit={handleSubmit}>
         <h2>Login</h2>

         <label>Username:</label>
         <input 
           value={username}
           onChange={(e)=>setEmail(e.target.value)}
         />

         <label>Password:</label>
         <input 
           type="password"
           value={password}
           onChange={(e)=>setpassword(e.target.value)}
         />

         <button type="submit">Login</button>
       </form>
     </div>
   );
}

export default Loginform;
