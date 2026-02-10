import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

import Register from '../pages/regiserter';
import Dashboard from '../pages/Dashboard';

import Loginform from '../pages/Loginform'
function App(){

    return(
        <BrowserRouter>


            <Routes>
                <Route path='/login' element={<Loginform/>}></Route>
                <Route path='/register' element={<Register />}></Route>
                <Route path='/dashboard' element={<Dashboard/>}></Route>
                <Route path='/' element={<Loginform/>}></Route>

            </Routes>
        </BrowserRouter>
    );
}

export default App