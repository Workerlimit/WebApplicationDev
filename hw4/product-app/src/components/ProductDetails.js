import React, {useState, useEffect, useMemo} from 'react';
import { fetchProduct } from './ProductService';

const ProductDetails = React.memo(({productId, quantity}) => {
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

    const addToBasket = () => {
        if(product) {
            alert("You have added this product to basket!");
        }
    }

    const calculatedPrice = useMemo(() => {
        if(product && quantity) {
            return product.price * quantity;
        }
        return 0;
    }, [product, quantity]);

    return (
        <div>
            <h1>Product Details</h1>
            {isLoading ? (<p>Loading...</p>) : product ? (
                <div>
                    <img src={product.image} alt={product.name} />
                    <h2>{product.name}</h2>
                    <p>{product.description}</p>
                    <p>Price: ${product.price}</p>
                    <p>Quantity: {quantity}</p>
                    <p>Total: ${calculatedPrice}</p>
                    <button onClick={addToBasket}>Add to basket</button>
                </div>
            ) : (<p>Product not found.</p>)}
        </div>
    );
});

export default ProductDetails;
