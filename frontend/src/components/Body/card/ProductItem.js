import React from 'react';

//Component used to display a product in the Home page
function ProductItem({ product }) {
    return (
        <div className="product_card">
            <img src={product[10]} alt="" />
            <div className="product_box">
                <h5 style={{fontSize:'18px', color:'#545454' , fontWeight:'800'}} title={product[2]}>{product[2]}</h5>
                <span style={{fontSize:'25px', fontWeight:'bold'}}>${product[9]}</span>
                <p style={{fontSize:'20px', fontWeight:'400', fontFamily:'Verdana'}}>Feedback Score: {product[6]}</p>

                {/* conditionally rendering an icon to recognize duplicated products  */}
                {product[11] === 'true' ? <img alt="duplicate" style={{ objectFit: 'contain', width: 40, height: 50, marginTop: -120, float: 'right' }} src="../../../Images/duplicate.png" /> : null}
            </div>
        </div>
    );
}

export default ProductItem;