import React from 'react';

//Display a duplicate products
function DuplicateItem({product}) {

    return (
        <div className="duplicate_product_card">
            <img src={product[9]} alt="" />
            <div>
                <h5 style={{fontSize:'18px', color:'#545454' , fontWeight:'800'}} title={product[1]}>{product[1]}</h5>
                <span style={{fontSize:'30px', fontWeight:'bold', color:'#C62828'}}>${product[8]}</span>
                <p style={{fontSize:'25px', fontWeight:'600', fontFamily:'inherit'}}>Feedback Score : {product[5]}</p>
                <button style={{fontSize:'25px',borderRadius:'8px', background:'#3E3C3C', width:'140px', height:'55px'}}>
                    <a href={product[3]} target="_blank" rel="noreferrer" style={{fontSize:'25px', color:'white'}}>Buy Now</a></button>
                </div>
            
            
            
        </div>
    )
}

export default DuplicateItem;