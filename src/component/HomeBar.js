import React from 'react'
import cLogo from "./assets/logo.png"
import eBay from "./assets/ebay.png"
import { BrowserRouter as Router, Route, NavLink } from "react-router-dom";
import Login from './Login';
import SignUp from './SignUp';

function HomeBar() {
    return (
        <div>
        <div className="homeBarMain">
        <Router>
            <div className="homeBar">
            <NavLink to="homePage" className="links">Home</NavLink> 
            </div>
            <ul className="loginBar">
                <li><NavLink to={"./Login"} className="links">Login&nbsp; |&nbsp;&nbsp;</NavLink></li>
                <li> <NavLink to={"./Login"} className="links">Sign up</NavLink></li>
            </ul>
            <Route path="/Login" component={Login} />
            <Route path="/SignUp" component={SignUp} />
        </Router>
        </div>
        <div>
            <div className="main-cover">
            <img src={cLogo} alt="logo" className="cLogo"/>
            <img src={eBay} alt="eBay" className="eBay"/>
            <p className="coverPara">
                Welcome to BuyLegit <br/><br/>
                BuyLegit helps you to pick an original product <br/>
                from eBay. We ensure you will always pay the<br/>
                original price and your choice of product is <br/>
                safe from over-priced listings.
            </p>
            
            </div>
        </div>
        </div>
    )
}

export default HomeBar
