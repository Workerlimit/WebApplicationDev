export const fetchProduct = (productId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (productId === 123) {
                resolve({
                    name: 'First Product',
                    description: 'Some product description.',
                    price: 29.99,
                    image: 'test.jpg',
                });
            } else {
                reject(new Error('Product not found.'));
            }
        }, 1000);
    });
};