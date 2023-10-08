export const fetchProduct = (productId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (productId === 123) {
                resolve({
                    name: 'First test project',
                    description: 'Some product description.',
                    price: 29.99,
                    image: 'https://images.pexels.com/photos/821651/pexels-photo-821651.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
                });
            } else {
                reject(new Error('Product not found.'));
            }
        }, 1000);
    });
};


