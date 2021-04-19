import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, NavLink } from 'react-router-dom';
import Route from 'react-router-dom/Route';
import NavBar from './components/NavBar';
import Cards from './components/Cards';
import CoverImage from './components/CoverImage';
import Footer from './components/Footer';
import Product from './components/Product';

const Home = () => {
  return(
    <div>
      <NavBar></NavBar>
      <CoverImage></CoverImage>
      <Cards></Cards>
      <Footer></Footer>
    </div>
  );
} 

function App() {
  return (
    <Router>
        <div className="App">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <div class="container-fluid">
          <ul class="navbar-nav me-auto mb-2 mb-lg-2">
            <li class="nav-item">
              <NavLink to="/">Home</NavLink>
            </li>
            <li class="nav-item">
              <NavLink to="/about">About</NavLink>
            </li>
            <li class="nav-item">
              <NavLink to="/contact">Contact</NavLink>
            </li>
            <li class="nav-item">
              <NavLink to="/log-in">LogIn</NavLink>
            </li> 
          </ul>
            
          </div>
        </nav>
          
          <Route path="/" exact strict component={ Home }/>
          <Route path="/product" exact strict component={ Product }/>

          <Route path="/about" exact strict render={()=>{
            return (<h1>About</h1>)
          }
          }/>

          <Route path="/contact" exact strict render={()=>{
            return (<h1>Contacts</h1>)
          }
          }/>

          <Route path="/log-in" exact strict render={()=>{
            return (<h1>Login</h1>)
          }
          }/>

      </div>
    </Router>
    
  );
}

export default App;
