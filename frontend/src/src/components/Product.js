import React,{useEffect,useState} from 'react';
import NavBar from './NavBar';
import CoverImage from './CoverImage';
import Footer from './Footer';
import axios from 'axios';

export const Product = (props) => {
    const [data,setData]=useState([]);
    const [isDuplicate,setIsDuplicate]=useState(false);
    const [dupData,setDupData] = useState([]);
    const itemId = props.location.aboutProps.itemId;

    //Use this only for testing
    //const productUrl = "http://127.0.0.1:5000/product/unique?itemId=114690047600";
    //const duplicatesUrl = "http://127.0.0.1:5000/product/duplicate?itemId=114690047600";

    const duplicatesUrl = "http://127.0.0.1:5000/product/duplicate?itemId="+itemId;
    const productUrl = "http://127.0.0.1:5000/product/unique?itemId="+itemId;
    
    const fetchItemDuplicateData = async () => {
        const response = await axios.get(duplicatesUrl);
        setDupData(response.data);
    };

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
    },[itemId]);
    return (
        <div>
            <NavBar />
            <CoverImage/>
                <div className="card text-center shadow">
                    <img src={data[10]} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h5 className="card-title">{data[2]}</h5>
                        <p className="card-text">Item ID: {data[0]}</p>
                        <p className="card-text">Price: {data[9]}</p>
                        <p className="card-text">Feedback Score: {data[6]}</p>
                        <p className="card-text">Positive Feedback Percentage: {data[7]}</p>
                        <p className="card-text">Seller's Username: {data[5]}</p>
                    </div>
                </div>
                {isDuplicate &&(
                <div>
                    {dupData.map((data,key)=>{
                        return(
                                <div className="col-md-3">
                                    <div className="card border-info h-100 text-center shadow">
                                        <img src={data[9]} className="card-img-top" alt="..."/>
                                        <div className="card-body" key={key}>
                                            <h5 className="card-title">{data[1]}</h5>
                                            <p className="card-text">Item ID: {data[0]}</p>
                                            <p className="card-text">Price: {data[8]}</p>
                                            <p className="card-text">Feedback Score: {data[5]}</p>
                                            <p className="card-text">Positive Feedback Percentage: {data[6]}</p>
                                            <p className="card-text">Seller's Username: {data[4]}</p>
                                        </div>
                                    </div>
                            </div>
                        );
                    })}
                </div>
                )}
                
            <Footer/>
            
        </div>
    );
}

export default Product;
