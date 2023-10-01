import React, { useState, useEffect } from 'react';
import { fetchProduct } from './ProductService';

function ProductDetails({ productId }) {
    const [product, setProduct] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await fetchProduct(productId);
                setProduct(data);
                setIsLoading(false);
            } catch (error) {
                console.error('Error fetching product:', error);
                setIsLoading(false);
            }
        };

        fetchData();
    }, [productId]);

    return (
        <div>
            <h1>Product Details</h1>
            {isLoading ? (<p>Loading...</p>) : product ? (
                <div>
                    <img src={product.image} alt={product.name} />
                    <h2>{product.name}</h2>
                    <p>{product.description}</p>
                    <p>Price: ${product.price}</p>
                </div>
            ) : (<p>Product not found.</p>)}
        </div>
    );
}

export default ProductDetails;
