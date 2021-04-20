import React from 'react'
import {useState} from 'react'

function NavBar({handleDropdownChange,handleCategory}) {

    return (
        <div>
            <nav class="navbar navbar-dark bg-dark fixed-top navbar navbar-expand-lg justify-content-between">
                <a class="navbar-brand">Home</a>
                <form class="form-inline">
                    <li id="category-drop-down">
                        <select className="sorting-options" placeholder="Category" onChange={(e)=>handleDropdownChange(e.target.value)} >
                            <option value="" disabled selected hidden placeholder="Category">Sort by</option>
                            <option value ="price" >Sort by Price</option>
                            <option value="score">Sort by Feedback Score</option>
                        </select>
                    </li>
                    <li id="category-drop-down">
                        <select className="sorting-options" placeholder="Category" onChange={(e)=>handleCategory(e.target.value)}>
                            <option value="" disabled selected hidden placeholder="Category">Category</option>
                            <option value="volvo">iPhone Covers</option>
                            <option value="saab">Watches</option>
                        </select>
                    </li>
                    <input class="form-control mr-sm-2" type="search" placeholder="Enter Product Name" aria-label="Search"/>
                    <button class="btn btn-outline-success my-2 my-sm-0 btn-lg" type="submit">Search</button>
                </form>
            </nav>
        </div>
    )
}

export default NavBar
