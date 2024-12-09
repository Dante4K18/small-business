import React, { useState, useEffect } from "react";
import axios from "axios";

function SupplierList() {
  const [suppliers, setSuppliers] = useState([]); // Initialize as an empty array

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/suppliers/")
      .then((response) => {
        console.log("Response data:", response.data); // Verify response structure
        setSuppliers(Array.isArray(response.data.data) ? response.data.data : []); // Access the array
      })
      .catch((error) => {
        console.error("Error fetching suppliers:", error);
      });
  }, []);

  return (
    <div>
      <h2>Supplier List</h2>
      <ul>
        {suppliers.length > 0 ? (
          suppliers.map((supplier) => (
            <li key={supplier.id}>
              {supplier.name} - {supplier.contact_info}
            </li>
          ))
        ) : (
          <li>No suppliers available</li>
        )}
      </ul>
    </div>
  );
}

export default SupplierList;
