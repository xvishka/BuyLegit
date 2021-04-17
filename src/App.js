import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/NavBar';
import Cards from './components/Cards';
import CoverImage from './components/CoverImage';
import Footer from './components/Footer';
import Pagination from './components/Pagination';

function App() {
  return (
    <div className="App">
      <NavBar></NavBar>
      <CoverImage></CoverImage>
      <Pagination></Pagination>
      <Cards></Cards>
      <Footer></Footer>
      
    </div>
  );
}

export default App;
