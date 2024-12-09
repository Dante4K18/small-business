import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

function OrderForm() {
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const initialValues = {
    product_id: "",
    quantity: "",
    status: "Pending",
  };

  const validationSchema = Yup.object({
    product_id: Yup.number()
      .required("Product ID is required")
      .positive("Product ID must be a positive number"),
    quantity: Yup.number()
      .required("Quantity is required")
      .positive("Quantity must be a positive number"),
    status: Yup.string()
      .required("Status is required")
      .oneOf(["Pending", "Shipped", "Delivered"], "Invalid status"),
  });

  const handleSubmit = (values, { setSubmitting }) => {
    setError(null); // Reset any previous errors
    const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";
  
    axios
      .post(`${API_URL}/orders`, values)
      .then(() => {
        navigate("/orders");
      })
      .catch((error) => {
        // Log the full error to the console for debugging purposes
        console.error("Error submitting order:", error);
  
        // Check if error.response exists and extract the message
        const errorMessage =
          error.response?.data?.error || error.message || "Something went wrong!";
  
        setError(errorMessage);  // Display the error message
        setSubmitting(false);     // Reset submitting state
      });
  };
  return (
    <div>
      <h2>Add Order</h2>
      {error && <div className="error">{error}</div>}
      <Formik
        initialValues={initialValues}
        onSubmit={handleSubmit}
        validationSchema={validationSchema}
      >
        {({ isSubmitting }) => (
          <Form>
            <div>
              <Field
                type="number"
                name="product_id"
                placeholder="Product ID"
                required
                min="1"
              />
              <ErrorMessage
                name="product_id"
                component="div"
                className="error"
                aria-live="polite"
              />
            </div>
            <div>
              <Field
                type="number"
                name="quantity"
                placeholder="Quantity"
                required
                min="1"
              />
              <ErrorMessage
                name="quantity"
                component="div"
                className="error"
                aria-live="polite"
              />
            </div>
            <div>
            <Field as="select" name="status" defaultValue="Pending">
            <option value="Pending">Pending</option>
            <option value="Shipped">Shipped</option>
            <option value="Delivered">Delivered</option>
            </Field>
              <ErrorMessage
                name="status"
                component="div"
                className="error"
                aria-live="polite"
              />
            </div>
            <button
              type="submit"
              disabled={isSubmitting}
              aria-busy={isSubmitting}
            >
              {isSubmitting ? "Submitting..." : "Add Order"}
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default OrderForm;
