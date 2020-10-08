import React from "react";
import Header from "./layout/Header";
import ProductsList from "./products/ProductsList";

const App = () => {
  return (
    <>
      <Header />
      <div className="container-fluid mt-4">
        <ProductsList />
      </div>
    </>
  );
};

export default App;
