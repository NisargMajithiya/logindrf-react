import './Dashboard.css';
import { ping } from '../services/apis';

function Dashboard(){

    async function testping() {

        try{
            const response = await ping();
            console.log("ping successful");
            alert("ping is successful")            
        } catch(error) {
            console.error("Ping failed:", error);
            alert("Ping failed! Check console.");
        }
        
    }


    return(
        <>
            <h2 id='dashboard'>Dashboard page</h2>
            <button onClick={testping}>test protected ping</button>
        </>
    );
}

export default Dashboard;
