# Inventory Management Application

An interactive and user-friendly inventory management system designed for small businesses. The application allows users to track products, manage suppliers, and handle orders efficiently.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features
- **Dashboard**: Overview of inventory statistics.
- **Product Management**: Add, update, and delete products.
- **Supplier Management**: Maintain a list of suppliers.
- **Order Management**: Create and track orders.
- **Search and Filtering**: Search through inventory with ease.
- **Responsive Design**: Optimized for desktops, tablets, and mobile devices.

---

## Technologies Used
- **Frontend**:
  - HTML, CSS (including vibrant styling for enhanced UX)
  - React.js for dynamic and interactive components
  - React Router for seamless navigation
- **Backend**:
  - Flask (for API handling)
  - SQLAlchemy (for database management)
- **Styling Framework**:
  - Google Fonts (Roboto)

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone \wsl.localhost\Ubuntu\home\dan\code\Development\small-business
   ```
2. Navigate to the project directory:
   ```bash
   cd small-business
   ```
3. Install frontend dependencies:
   ```bash
   npm install
   ```
4. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the backend server:
   ```bash
   flask run
   ```
6. Start the frontend development server:
   ```bash
   npm start
   ```

---

## Usage
1. Launch the application in your browser.
2. Use the navbar to navigate between products, suppliers, and orders.
3. Add, update, or delete entries as needed.
4. Search for specific inventory items using the search bar.

---

## Folder Structure
```
small-business
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── styles
│   │   └── App.js
├── backend
│   ├── app.py
│   ├── models.py
│   └── migrations
├── README.md
└── requirements.txt
```

---

## Future Enhancements
- Add role-based authentication.
- Export inventory data to CSV or Excel.
- Integrate analytics and reporting tools.
- Introduce multi-language support.

---

## License
This project is licensed under the [MIT License](LICENSE).

