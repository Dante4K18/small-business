import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
// import Navbar from './components/Navbar';
import Dashboard from "./components/Dashboard";
import ProductList from "./components/ProductList";
import ProductForm from "./components/ProductForm";
import SupplierList from "./components/SupplierList";
import SupplierForm from "./components/SupplierForm";
import OrderList from "./components/OrderList";
import OrderForm from "./components/OrderForm";
import Navbar1 from "./components/Navbar1";

function App() {
  return (
    <Router>
      {/* <Navbar /> */}
      <Navbar1/>
      <div className="App">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/products" element={<ProductList />} />
          <Route path="/products/add" element={<ProductForm />} />
          <Route path="/suppliers" element={<SupplierList />} />
          <Route path="/suppliers/add" element={<SupplierForm />} />
          <Route path="/orders" element={<OrderList />} />
          <Route path="/orders/add" element={<OrderForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
