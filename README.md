KCMS PROJECT
KCMS (Knowledge Content Management System) is a Django-based project built to demonstrate clean backend architecture, real-world permission handling, and professional REST API design using Django Rest Framework (DRF).
The project was developed with a strong focus on backend engineering fundamentals rather than UI.

This project contains both:

Traditional Django (HTML + CBVs)

REST APIs built using DRF (JWT-based)

The goal is to understand how Django and DRF coexist in real production systems.

PROJECT FEATURES
User authentication using Django auth system

Role-based access control (Admin, Staff, Public)

Ownership-based permissions

Category and Content management

REST APIs with JWT authentication

Object-level permissions in APIs

Optimized database queries

Clean separation between HTML views and API layer

TECH STACK
Python

Django

Django Rest Framework

JWT Authentication

SQLite (development)

Postman (API testing)

PROJECT STRUCTURE
CMS/
├── CMS/ Project settings
├── content/ Django HTML app
├── api/ DRF APIs
├── templates/ HTML templates
├── media/ Uploaded images
├── db.sqlite3
└── manage.py

CONTENT APP (DJANGO)
The content app implements traditional Django concepts using CBVs.

Key concepts covered:

Class Based Views

Mixins for permissions

LoginRequired, Staff, Admin access

Ownership-based access control

Queryset filtering based on user role

Pagination

Optimized queries using select_related

Models:

Category

Content

Permissions logic:

Admin: Full access

Staff: Create and manage own content

Public users: Read-only access to active content

API APP (DRF)
The api app exposes REST APIs without affecting HTML views.

Key concepts implemented:

Serializers (read vs write separation)

ViewSets and Routers

JWT Authentication

Custom permissions

Object-level permissions

Filtering, search, ordering

Pagination

Performance optimization

Important rule:
HTML views and DRF APIs are completely independent.

AUTHENTICATION
Django session authentication for HTML views

JWT authentication for APIs

API authentication uses access and refresh tokens.
Unauthenticated users have read-only access where applicable.

PERMISSIONS (API)
IsAuthenticated

DjangoModelPermissions

Custom permissions

Object-level permission checks

Permission rules:

Admin: Full access

Staff: Create and manage own resources

Public: Read-only access

PERFORMANCE CONSIDERATIONS
Avoided N+1 queries

Used select_related and prefetch_related

Serializer design prevents extra queries

Pagination applied to large datasets

HOW TO RUN LOCALLY
Clone the repository

Create virtual environment

Install dependencies

Run migrations

Create superuser

Start development server

Example commands:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

LEARNING OUTCOMES
This project demonstrates:

Real-world Django permission patterns

Professional DRF API design

JWT authentication flow

Clean backend architecture

Difference between Django views and DRF views

How production APIs are structured

AUTHOR
Built by Aashish Dangi
Purpose: Backend engineering practice and DRF mastery

END OF FILE
