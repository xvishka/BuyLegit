import React,{useEffect,useState} from 'react'
import axios from 'axios';
import NavBar from './NavBar';

const allProductsUrl = "http://127.0.0.1:5000/api/product/all";
const sortByPriceUrl = "http://127.0.0.1:5000/api/product/all/priceSort";
const sortByFeedbackScoreUrl = "http://127.0.0.1:5000/api/product/all/feedbackScoreSort"

function Cards() {
    const [Data,setData]=useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [productsPerPage, setProductsPerPage] = useState(20);
    const [navProp,setNavProp]=useState([{sort:"all"}]);
    const [sort,setSort]=useState("all");

    const handleDropdownChange=(e)=>{
        setSort(e);
        console.log(sort)
    }

    const fetchOriginalData = async () => {
        const response = await axios.get(allProductsUrl);
        setData(response.data);
    };

    const fetchDataSortedByPrice = async () => {
        const responseToPrice = await axios.get(sortByPriceUrl);
        setData(responseToPrice.data);
    };

    const fetchDataSortedByFeedbackScore = async () => {
        const response = await axios.get(sortByFeedbackScoreUrl);
        setData(response.data);
    };


    useEffect(()=>{
        if(sort==="all"){
            fetchOriginalData();
        }
        else if(sort==="price"){
            fetchDataSortedByPrice();
        }
        else if(sort==="score"){
            fetchDataSortedByFeedbackScore();
        }
    },[sort]);

    //Get current posts
    const indexOfLastProduct = currentPage * productsPerPage;
    const indexOfFirstProduct = indexOfLastProduct - productsPerPage
    const currentPosts = Data.slice(indexOfFirstProduct,indexOfLastProduct);

    return (
        <div>
            <NavBar nav={navProp} handleDropdownChange={handleDropdownChange}/>
            <div className="row">
                {currentPosts.map((data,key)=>{
                    return(
                        
                            <div className="col-md-3">
                                <div className="card border-info h-100">
                                    <img src={data.image} className="card-img-top" alt="..."/>
                                    <div className="card-body" key={key}>
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
                    );
                })}
            </div>
       </div>
    )
}

export default Cards
