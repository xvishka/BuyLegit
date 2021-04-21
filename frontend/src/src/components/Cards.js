import React,{useEffect,useState} from 'react'
import axios from 'axios';
import { Redirect } from 'react-router-dom';
import NavBar from './NavBar';
import Pagination from './Pagination';
import Product from './Product';
import history from './History';
import CoverImage from './CoverImage';
import Footer from './Footer';
import { Link } from "react-router-dom";

const allProductsUrl = "http://127.0.0.1:5000/product/all?categoryId=1";
const sortByPriceUrl = "http://127.0.0.1:5000//product/all/priceSort?categoryId=1";
const sortByFeedbackScoreUrl = "http://127.0.0.1:5000//product/all/feedbackScoreSort?categoryId=1"

const Cards = () => {
    
    const [Data,setData]=useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [productsPerPage, setProductsPerPage] = useState(20);
    const [navProp,setNavProp]=useState([{sort:"all"}]);
    const [sort,setSort]=useState("all");
    const [redirect, setRedirect] = useState(true);

    const handleDropdownChange=(e)=>{
        setSort(e);
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
    const indexOfFirstProduct = indexOfLastProduct - productsPerPage;
    const currentProducts = Data.slice(indexOfFirstProduct,indexOfLastProduct);

    //Change page
    const paginate = pageNumber => setCurrentPage(pageNumber);

    return (
        <div>
            <NavBar nav={navProp} handleDropdownChange={handleDropdownChange}/>
            <CoverImage/>
            <div className="row">
                {currentProducts.map((data,key)=>{
                    return(
                            <div className="col-md-3">
                                 <Link to={{pathname:"/product", aboutProps:{itemId:data[0]}}}>
                                <div className="card border-info h-100 text-center shadow">
                                    <img src={data[10]} className="card-img-top" alt="..."/>
                                    <div className="card-body" key={key}>
                                        <h5 className="card-title">{data[2]}</h5>
                                        <p className="card-text">Item ID: {data[0]}</p>
                                        <p className="card-text">Price: {data[9]}</p>
                                        <p className="card-text">Feedback Score: {data[6]}</p>
                                        <p className="card-text">Positive Feedback Percentage: {data[7]}</p>
                                        <p className="card-text">Seller's Username: {data[5]}</p>
                                        <p className="card-text">Duplicate: {data[11]}</p>
                                        
                                    </div>
                                </div>
                                </Link>
                        </div>
                    );
                })}
            </div>
            <Pagination productsPerPage={productsPerPage} totalProducts={Data.length} paginate={paginate}></Pagination>
            <Footer/>
       </div>
    )
}

export default Cards
