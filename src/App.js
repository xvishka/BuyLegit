import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/NavBar';
import Cards from './components/Cards';
import CoverImage from './components/CoverImage';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <NavBar></NavBar>
      <CoverImage></CoverImage>
      <Cards></Cards>
      <Footer></Footer>
      
    </div>
  );
}

export default App;
