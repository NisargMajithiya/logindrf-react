import { useAuth } from "../context/authcontext";

function Navbar(){
    const { user } = useAuth();
    return(
        <>
            navbar - {user? user.email : "Not Logged In"}
        </>
    );
}

export default Navbar;

