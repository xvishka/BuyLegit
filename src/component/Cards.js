import React,{useEffect,useState} from 'react'
import {Card} from 'react-bootstrap';
import CardDeck from "react-bootstrap/CardDeck";
// import ApicemData from './assets/ApicemData.json';
//import * as data from './assets/ApicemData.json';
import data from './assets/ApicemData.json';
import axios from 'axios';

const url = "http://127.0.0.1:5000/api/product/all"; 

const Cards=()=> {
    const productList=[];

    const [Data,setData]=useState([]);

    const getGitHubUserWithFetch = async () => {
        const response = await axios.get(url);
        setData(response.data);
        console.log(data)
      };

    useEffect(()=>{
        getGitHubUserWithFetch();
    },[]);

    return (
        <div>
            {Data.map((data,key)=>{
                return(
                    <div className ="card-deck">
                        <div className="card border-dark mb-3">
                            <img className="card-img-top" src={data.image} alt="Card image cap"/>
                            <div className="card-body">
                                <div key={key}>
                                    <h5 className="card-title">{data.title}</h5>
                                    <p className="card-text">Price: {data.price}</p>
                                    <p className="card-text">Feedback Score: {data.feedbackScore}</p>
                                    <p className="card-text">Positive Feedback Percentage: {data.positiveFeedbackPercent}</p>
                                    <p className="card-text">Seller's Username: {data.sellerUserName}</p>
                                    <p className="card-text">Shipping: {data.shipping}</p>
                                    <p className="card-text">Product No: {data.product}</p>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                   
                );
            })}
        </div>
    );
}

export default Cards
