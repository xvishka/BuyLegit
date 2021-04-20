import './App.css';
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Switch } from 'react-router-dom';
import Route from 'react-router-dom/Route';

import Cards from './components/Cards';
import Product from './components/Product';


function App() {
  return (
    
    <Router>
      <Switch>
      
          <Route path="/" exact component={ Cards }/>
          <Route path="/product" component={ Product }/>

      </Switch>
    </Router>
    
  );
}

export default App;
