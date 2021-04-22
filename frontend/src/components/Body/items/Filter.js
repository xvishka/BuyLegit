import React from 'react';

function Filter({ handleDropdownChange, handleSearch, handleCategoryChange, handleSort }) {
    return (
        <div className="filter_menu">
            <div className="row">
                <span style={{fontFamily:'helvetica', fontSize:'20px', fontWeight:'600', color:'#5A5A5A'}}>Filters: </span>
                <select className="category" id="filterBy" onChange={handleCategoryChange}>
                    <option value="1">iPhone X cases</option>
                    <option value="2">Smart Watches</option>
                    <option value="3">iPhone 7 cases</option>
                </select>
            </div>

            <input className="searchBar" type="text" placeholder=" Search ..." onChange={handleSearch} />

            <div className="row sort">
                <span style={{fontFamily:'helvetica', fontSize:'20px', fontWeight:'600', color:'#5A5A5A'}}>Sort By: </span>
                <select className="category" onChange={handleSort}>
                    <option value="rank">Rank</option>
                    <option value="price">Price</option>
                    <option value="score">Feedback Score</option>
                </select>
            </div>
        </div>
    );
}

export default Filter;