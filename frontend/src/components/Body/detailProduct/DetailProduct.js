import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import DuplicateItem from '../card/DuplicateItem';
import axios from 'axios';

//Component used to display further details about selected product
function DetailProduct() {
    
    const params = useParams();
    const [data,setData]=useState([]);
    const [isDuplicate,setIsDuplicate]=useState(false);
    const [dupData,setDupData] = useState([]);

    //API calls from the hosted backend
    const productUrl = "https://buylegit-1.herokuapp.com/product/unique?itemId="+params.id;
    const duplicatesUrl = "https://buylegit-1.herokuapp.com/product/duplicate?itemId="+params.id;

    //Function used to fetch duplicate product data
    const fetchItemDuplicateData = async () => {
        const response = await axios.get(duplicatesUrl);
        setDupData(response.data);
    };

    //Function used to fetch all uniqie product data
    const fetchItemData = async () => {
        const response = await axios.get(productUrl);
        setData(response.data[0]);
        if(response.data[0][11] === "true"){
            fetchItemDuplicateData();
            setIsDuplicate(true);
        }
    };

    useEffect(()=>{
        fetchItemData();
    },);

    return (
        <>
            <div className="detail">
                <img src={data[10]} alt="" />
                <div className="box-detail">
                    <div className="row">
                        <h4 className="title">{data[2]}</h4>
                    </div>
                    <p style={{fontSize:'23px', fontWeight:'600', fontFamily:'inherit'}}>Item ID: {data[0]}</p>
                    <span style={{fontSize:'30px', fontWeight:'bold', color:'#C62828'}}>$ {data[9]}</span>
                    <p style={{fontSize:'23px', fontWeight:'600', fontFamily:'inherit'}}>Seller : {data[5]}</p>
                    <p style={{fontSize:'23px', fontWeight:'600', fontFamily:'inherit'}}>FeedbackScore      : {data[6]}</p>
                    <p style={{fontSize:'23px', fontWeight:'600', fontFamily:'inherit'}}>Positive Percentage: {data[7]}</p>
                    <button className="cart" style={{fontSize:'25px',borderRadius:'8px', color:'white'}}>
                        <a href={data[4]} target="_blank" rel="noreferrer" style={{fontSize:'25px', color:'white'}}  >Buy Now</a></button>
                </div>
            </div>

            {isDuplicate &&(
                <div>
                    <h2>Duplicate Products</h2>
                    <div className="products">
                        {
                            dupData.map(dupData =>  {return(
                               <DuplicateItem key={dupData[0]} product={dupData} />
                            )})
                        }
                    </div>
                </div>)
            }
        </>
    )
}

export default DetailProduct