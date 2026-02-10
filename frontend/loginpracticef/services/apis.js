import axios from "axios";

const api = axios.create({
    baseURL:"http://127.0.0.1:8000/api",
    headers :{
        
    },
});

export default api;

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access');
        console.log("INTERCEPTOR RUNNING");
        console.log("TOKEN",token);

         if (
            config.url.includes("/login") ||
            config.url.includes("/register")
        ) {
            return config;
        }
        
        
        if (token) {
            config.headers = config.headers || {};
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export const loginapi = async(username,password) => {
    return api.post("/login/",{
        username,
        password,

    });
};

export const registerapi = async(username,email,phone_number,password) =>{
    return api.post("/register",{
        username,
        email,
        phone_number,
        password
    });
}

export const ping = async() =>{
    return api.get("/ping/");
};