# 🛒 AMAZON INDIA — E-COMMERCE CLONE

> **A meticulously crafted Django-based recreation of a contemporary Indian e-commerce experience — conceived as a Semester 3 Web Development project.**

![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## ✦ Overview

**AMAZON INDIA — E-COMMERCE CLONE** is a deliberately scoped, locally runnable e-commerce web application developed with **Django, SQLite, HTML, CSS, and JavaScript**.

The project attempts to recreate the **interaction patterns and visual grammar of a contemporary e-commerce platform** while retaining an intentionally modest architectural footprint suitable for an undergraduate Web Development project.

Rather than pursuing needless infrastructural complexity, the application concentrates on the fundamentals that constitute a convincing commerce experience:

**discovery → evaluation → cart → checkout → order history**

The result is a self-contained academic implementation that demonstrates how a conventional web application can be structured from the ground up.

---

## ✧ What It Contains

### 🏠 Immersive Homepage
- Amazon-inspired navigation interface
- Search bar and category navigation
- Hero carousel with automatic transitions
- Category discovery section
- Deals and recommended products
- Responsive layout

### 🔎 Product Discovery
- Product catalogue
- Keyword-based search
- Category filtering
- Price sorting
- Rating sorting
- Product availability indicators
- Discount calculations

### 📦 Product Experience
- Dedicated product-detail pages
- Product descriptions
- Pricing and previous pricing
- Ratings and review counts
- Stock information
- Add-to-cart functionality

### 🛍️ Cart
- Add products
- Remove products
- Modify quantities
- Automatic subtotal calculation
- Cart total calculation

### 🔐 Authentication
- User registration
- Login
- Logout
- Django's built-in authentication framework

### 💳 Checkout
- Delivery information
- Order summary
- Mock payment-method selection
- Order placement

> **Payment processing is intentionally simulated. No real financial transaction is performed.**

### 📋 Orders
- Personal order history
- Individual order details
- Purchased items
- Quantities and subtotals
- Order status
- Timestamped orders

---

## ⚙️ Technology Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.1 |
| Language | Python |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite |
| Authentication | Django Authentication |
| Styling | Custom CSS |
| Client-side Behaviour | Vanilla JavaScript |

---

## 🧭 Application Flow

```text
                 ┌─────────────────┐
                 │     Homepage    │
                 └────────┬────────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        Categories     Search       Products
             │            │            │
             └────────────┼────────────┘
                          ▼
                  Product Details
                          │
                          ▼
                    Add to Cart
                          │
                          ▼
                       Cart
                          │
                          ▼
                      Checkout
                          │
                          ▼
                  Order Confirmation
                          │
                          ▼
                    Order History
