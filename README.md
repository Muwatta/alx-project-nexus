# E-Commerce Backend API – Django REST Framework

## Description

Production-ready backend for an e-commerce platform that supports product catalogs, orders, checkout, user authentication, and asynchronous operations. Designed for scalability, maintainability, and integration with frontend applications.

---

## Features

* JWT authentication with role-based access control
* Product and category CRUD management
* Order lifecycle management and checkout workflow
* Filtering, sorting, and pagination for large datasets
* Background tasks (email notifications, order processing) using Celery and RabbitMQ
* Redis caching for performance optimization
* Dockerized for consistent development and production environments
* CI/CD pipelines using GitHub Actions for automated testing and deployment

---

## Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** PostgreSQL
* **Caching:** Redis
* **Async Tasks:** Celery + RabbitMQ
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Authentication:** JWT with role-based permissions

---

## Architecture Overview

* `accounts` – Handles user authentication and management
* `catalog` – Manages products and categories
* `orders` – Handles order processing and tracking
* `checkout` – Payment integration and order confirmation
* `backend` – Project configuration and settings

---

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/Muwatta/alx-project-nexus.git
cd alx-project-nexus
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

* `POSTGRES_DB`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `SECRET_KEY`

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```

6. For Docker:

```bash
docker-compose up --build
```

---

## Authentication

* JWT access and refresh tokens
* Role-based permissions: Admin, Customer, Staff
* Passwords hashed securely with Django’s built-in authentication system

---

## Background Tasks

* Asynchronous email notifications
* Order processing tasks
* Handled by Celery and RabbitMQ

---

## API Endpoints (Summary)

* `/api/accounts/` – User registration, login, and profile management
* `/api/catalog/products/` – CRUD operations for products
* `/api/catalog/categories/` – CRUD operations for categories
* `/api/orders/` – Create, retrieve, and manage orders
* `/api/checkout/` – Payment and order confirmation

---

## Deployment

* Dockerized application ensures consistent environments
* CI/CD pipelines using GitHub Actions automate testing, building, and deployment

---

## Project Status

Actively maintained as part of the ALX ProDev Backend Engineering Capstone.

---

## GitHub Repository

[https://github.com/Muwatta/alx-project-nexus](https://github.com/Muwatta/alx-project-nexus)
