import React from 'react';
import Items from './items/Items';
import About from './about/About';
import DetailProduct from './detailProduct/DetailProduct';
import {Switch,Route} from 'react-router-dom';

function Pages() {
    return (
        <Switch>
            <Route path="/" exact component={Items}/>
            <Route path="/about" exact component={About}/>
            <Route path="/detail/:id" exact component={DetailProduct} />
        </Switch>
    )
}

export default Pages