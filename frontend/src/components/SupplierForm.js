import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Formik, Form, Field } from "formik";

function SupplierForm() {
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const initialValues = {
    name: "",
    contact_info: "",
    address: ""
  };

  const handleSubmit = (values) => {
    axios.post("http://127.0.0.1:5000/suppliers/", values)
      .then(() => {
        navigate("/suppliers");
      })
      .catch((error) => {
        setError(error.response.data.error);
      });
  };

  return (
    <div>
      <h2>Add Supplier</h2>
      {error && <div className="error">{error}</div>}
      <Formik
        initialValues={initialValues}
        onSubmit={handleSubmit}
      >
        <Form>
          <div>
            <Field type="text" name="name" placeholder="Supplier Name" required />
          </div>
          <div>
            <Field type="text" name="contact_info" placeholder="Contact Info" />
          </div>
          <div>
            <Field type="text" name="address" placeholder="Address" />
          </div>
          <button type="submit">Add Supplier</button>
        </Form>
      </Formik>
    </div>
  );
}

export default SupplierForm;
