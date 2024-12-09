import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Formik, Form, Field } from "formik";

function ProductForm() {
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const initialValues = {
    name: "",
    description: "",
    price: "",
    stock_quantity: "",
    supplier_id: ""
  };

  const handleSubmit = (values) => {
    axios.post("http://127.0.0.1:5000/products/", values)
      .then(() => {
        navigate("/products");
      })
      .catch((error) => {
        setError(error.response.data.error);
      });
  };

  return (
    <div>
      <h2>Add Product</h2>
      {error && <div className="error">{error}</div>}
      <Formik
        initialValues={initialValues}
        onSubmit={handleSubmit}
      >
        <Form>
          <div>
            <Field type="text" name="name" placeholder="Product Name" required />
          </div>
          <div>
            <Field type="text" name="description" placeholder="Description" />
          </div>
          <div>
            <Field type="number" name="price" placeholder="Price" required />
          </div>
          <div>
            <Field type="number" name="stock_quantity" placeholder="Stock Quantity" required />
          </div>
          <div>
            <Field type="number" name="supplier_id" placeholder="Supplier ID" required />
          </div>
          <button type="submit">Add Product</button>
        </Form>
      </Formik>
    </div>
  );
}

export default ProductForm;
