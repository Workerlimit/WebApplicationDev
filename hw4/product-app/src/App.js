import React from 'react';
import ProductDetails from './components/ProductDetails';
import withAuthentication from './components/withAuthentication';

function App() {
  return (
      <div className="App">
        <h1>E-commerce App</h1>
        <ProductDetails productId={123} quantity={10} />
      </div>
  );
}

export default withAuthentication(App);
