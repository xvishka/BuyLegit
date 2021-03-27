import React from 'react'
import logo from "./assets/logo.png"

function NavBar() {
    return (
        <div>
            <nav>
                <div className="logo">
                    <img src={logo} alt="logo" className="logoImg"/>
                </div>
                <ul className="nav-options">
                    <li>
                    <form>
                        <input type="text" className="searchProduct" name="searchText" placeholder="Search ..."/>
                        
                    </form>
                    </li>
                     
                    <li>
                        <select className="options" placeholder="Category">
                        <option value="" disabled selected hidden placeholder="Category">Category</option>
                        <option value="volvo">iPhone Covers</option>
                        <option value="saab">Watches</option>
                        </select>
                    </li>
                    
                </ul>
            </nav>
        </div>
    )
}

export default NavBar
