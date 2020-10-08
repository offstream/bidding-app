import React from "react";

const ProductItem = ({ name, description = "", created_at, image }) => {
  return (
    <div className="card mb-3 mx-1" style={{ maxWidth: "540px" }}>
      <div className="row no-gutters">
        <div className="col-md-3">
          <img src={image} className="card-img" alt="Cakes and Lies" />
        </div>
        <div className="col-md-8">
          <div className="card-body">
            <h5 className="card-title">{name}</h5>
            <p className="card-text">{description}</p>
            <p className="card-text">{description}</p>
            <p className="card-text">
              <small className="text-muted">Created: {created_at}</small>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductItem;
