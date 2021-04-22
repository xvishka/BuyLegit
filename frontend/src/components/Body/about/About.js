import React from 'react';

function About() {

    return (
        <div>
            <div style={{textAlign:'center'}}>
            <span style={{ fontSize:50, fontFamily:'monospace', color:'#5A5A5A'}}>Hello!</span><br></br>
            <div style={{height:'6px', backgroundColor:'#9F9F9F', marginBottom:'20px'}} ></div>
            <div style={{width:'65%',marginLeft:'18%',fontFamily:'Candara',fontSize:'25px'}}>
            Welcome to BuyLegit. We are here to support you when you shop through the internet. 
            At BuyLegit we have developed a system to filter all products on an ecommerce platform, 
            we carefully identify the same product repeated multiple times. we analyse them through multiple criterias 
            and here we have presented you the best products out of them. we invite you to shop through BuyLegit and save your time, 
            money and have a quality product delivered to you !
            </div>

            </div>
            <img src='Images\aboutIcon.png' alt="about" style={{marginLeft:'42%'}}/> <br></br>
            <a href = 'mailto:thiranhettiarachchi@gmail.com'><h1 style={{textAlign:'center',color:'teal'}}>Developed by Apicem</h1></a>
        </div>
    )
}

export default About
