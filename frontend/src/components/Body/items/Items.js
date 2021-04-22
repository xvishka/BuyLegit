import React, { useEffect, useState } from 'react';
import ProductItem from '../card/ProductItem';
import axios from 'axios';
import Filters from './Filter';
import { Link } from 'react-router-dom';

//Component used to display all the products in the home page
function Items() {
    
    const allProductsUrl = 'https://buylegit-1.herokuapp.com/product/all?categoryId=1';
    const searchApi = 'https://buylegit-1.herokuapp.com/product/search';
    const categoryApi = 'https://buylegit-1.herokuapp.com/product/all';

    const sortByPriceUrl = "https://buylegit-1.herokuapp.com/product/all/priceSort";
    const sortByFeedbackScoreUrl = "https://buylegit-1.herokuapp.com/product/all/feedbackScoreSort";

    const [products, setProducts] = useState([]);

    const handleOnSort = async event => {
        if(event.target.value === "price") {
            const response = await axios.get(`${sortByPriceUrl}`, {
                params: {
                    categoryId: 1,
                },
            });
            setProducts(response.data);
        } else if (event.target.value === "score") {
            const response = await axios.get(`${sortByFeedbackScoreUrl}`, {
                params: {
                    categoryId: 1,
                }
            })
            setProducts(response.data);
        } else {
            fetchOriginalData();
        }

    };

    const fetchOriginalData = async () => {
        const response = await axios.get(allProductsUrl);
        setProducts(response.data);
    };

    const fetchSearchData = async event => {
        const response = await axios.get(`${searchApi}`, {
            params: {
                title: event.target.value,
            },
        });
        setProducts(response.data);
    };

    const fetchCatergoryData = async event => {
        const response = await axios.get(`${categoryApi}`, {
            params: {
                categoryId: event.target.value,
            },
        });
        setProducts(response.data);
    };

    useEffect(() => {
        fetchOriginalData();
    }, []);

    return (
        <>
            <Filters handleSort={handleOnSort} handleSearch={fetchSearchData} handleCategoryChange={fetchCatergoryData} />

            <div className="products">
                {(products || []).map(product => {
                    return (
                        <div key={product[0]} >
                            {' '}
                            <Link id="btn_view" to={`/detail/${product[0]}`} style={{ textDecoration: 'none', color: 'inherit' }}>
                                <ProductItem product={product} />
                            </Link>
                        </div>
                    );
                })}
            </div>
        </>
    );
}

export default Items;