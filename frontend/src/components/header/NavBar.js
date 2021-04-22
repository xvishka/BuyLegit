import React from 'react';
import Menu from './headerIcon/navBar.svg';
import Close from './headerIcon/close.svg';
import { Link } from 'react-router-dom';


function NavBar() {
    
    return (
       <header >
           <img src={Menu} alt="Mobile Bar" className="menu" width="30" /> 
           <div className="logo">
           <Link to="/"><img width='450px' src='../../../Images/logo.png' alt="logo"/></Link>
           </div>
           <ul>
               <li><Link to="/" style={{fontSize:'25px', fontWeight:'bold'}}>Home</Link></li>
               <li><Link to="/about" style={{fontSize:'25px', fontWeight:'bold'}}>About</Link></li>
               <li>
                   <img src={Close} alt="closeBtn" width="30" className="menu" />
               </li>
           </ul>
                      

       </header>
    )
}

export default NavBar