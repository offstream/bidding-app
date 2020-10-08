import React from "react";
import ProductItem from "./ProductItem";
import { useFetch } from "../../hooks/useFetch";

const ProductsList = () => {
  const { data: products, loading } = useFetch(
    "http://localhost:8000/api/products/"
  );
  return (
    <div className="d-flex flex-row flex-wrap justify-content-around">
      {!loading &&
        products.map(product => <ProductItem key={product.id} {...product} />)}
    </div>
  );
};

export default ProductsList;
