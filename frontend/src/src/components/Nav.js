import React from "react";
import Svg from '../assets/images/Frame_1.svg';
import './Nav.css';


function Nav(){
    return(
        <div className="site-nav grid">
            <div className="logo">
                <img src={Svg} alt="React Logo"/>
            </div>
            <form>
                <input type="text"/>
            </form>
        </div>
    );
}

export default Nav;