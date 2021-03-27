import React from 'react';
import logoFooter from "./assets/logo.png"

function Footer() {
    return (
        <div>
            <footer>
                <div className="footerCol">
                    <div className="colOne">
                        <img src={logoFooter} alt="logo" className="logoF"/>
                    </div>
                    {/* <ul className="footer-options">
                        <li>Home</li>
                        <li>Categories</li>
                        <li>Visit eBay</li>
                    </ul> */}
                </div>
            </footer>
        </div>
    )
}

export default Footer

