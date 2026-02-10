import { useContext, createContext, useState } from "react";
import { loginapi } from "../services/apis";

const AuthContext = createContext();

const AuthProvider = ({ children }) =>{
    const [refresstoken,setrefresstoken] = useState(null);
    const [token,setToken] = useState(null);

    const login = async(username,password) => {
        try{
            const response = await loginapi(username,password);

            const access = response.data.access;
            const refreshtoken = response.data.refresh;

            setToken(access);
            localStorage.setItem("access",access);
            setrefresstoken(refreshtoken);

            console.log(access);
            console.log(refreshtoken);
            
            

            
            

            return true;

        } catch(error){
            console.log("login error",error);
            return false
            
        }
    };

    // const regiter =

    return <AuthContext.Provider value={{refresstoken,token,login}}>{children}</AuthContext.Provider>;

};

export default AuthProvider;

export const useAuth = () => {
  return useContext(AuthContext);
};

