import React from 'react'

export const Product = (props) => {
    return (
        <div>
            <div className="card text-center shadow">
                <img src={props.imageUrl} className="card-img-top" alt="..."/>
                <div className="card-body">
                    <h5 className="card-title">{props.title}</h5>
                    <p className="card-text">Price: {props.price}</p>
                    <p className="card-text">Feedback Score: {props.feedbackScore}</p>
                    <p className="card-text">Positive Feedback Percentage: {props.positiveFeedbackPercentage}</p>
                    <p className="card-text">Seller's Username: {props.sellerUserName}</p>
                    <p className="card-text">Shipping: {props.shipping}</p>
                </div>
            </div>
            
        </div>
    );
}

export default Product
