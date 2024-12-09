import React from "react";
import ReactDOM from "react-dom/client"; // Import from 'react-dom/client' in React 18
import App from "./App";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root")); // Create root instead of render
root.render(<App />); // Use render on the root
