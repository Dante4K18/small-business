import React, { useState, useEffect } from "react";
import axios from "axios";
import OrderForm from "./OrderForm";

function OrderList() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/orders/")
      .then((response) => {
        setOrders(response.data);
      })
      .catch((error) => console.error("Error fetching orders:", error));
  }, []);

  return (
    <div>
      <h2>Order List</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>
            Order ID: {order.id}, Status: {order.status}
          </li>
        
        ))}
      </ul>
      <div>
          <OrderForm />
        </div>
    </div>
  );
}

export default OrderList;
