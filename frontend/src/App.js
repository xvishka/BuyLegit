import React from 'react';
import {BrowserRouter as Router} from 'react-router-dom';
import Pages from './components/Body/Pages';
import NavBar from './components/header/NavBar';


function App() {
  return (
    <Router>
      <div className="App" style={{backgroundColor:'#EDEDED'}}>
          <NavBar/>
          <Pages/>
      </div>

    </Router>
  );
}

export default App;
