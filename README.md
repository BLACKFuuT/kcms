# KCMS – Knowledge Content Management System

KCMS is a backend-focused Django project built to develop a strong, production-ready understanding of **Django** and **Django REST Framework (DRF)**.  
The project is intentionally designed to separate **traditional Django (HTML views)** from **REST APIs**, mirroring how real-world systems are structured.

This repository is not a tutorial project. It is an engineering practice project.

---

## Purpose of the Project

- Build a clean, maintainable Django codebase
- Understand Django vs DRF at a conceptual level
- Implement authentication and authorization correctly
- Design APIs with scalability and performance in mind
- Practice real-world permission and ownership patterns
- Reach engineer-level confidence with DRF

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite (development)
- Postman for API testing

---

## High-Level Architecture

The project uses **two clearly separated layers**:

1. Django HTML Layer  
2. Django REST Framework API Layer  

These layers share models but do not depend on each other.

---

## Project Structure
CMS/
├── CMS/ # Project settings, URLs, WSGI
├── content/ # Django HTML app (CBVs, templates, mixins)
├── api/ # DRF app (serializers, viewsets, permissions)
├── templates/ # HTML templates
├── media/ # Uploaded files
├── db.sqlite3
└── manage.py


Rule:  
HTML views must never depend on DRF code.  
DRF APIs must never depend on templates.

---

## Django Layer (HTML Views)

The `content` app is implemented using Django Class-Based Views and custom mixins.

### Features

- User authentication (login, logout, signup)
- Role-based access control
- Ownership-based permissions
- Category management
- Content management
- Pagination
- Optimized queryset handling

### Roles

- Admin  
  Full access to categories, users, and content

- Staff  
  Can create content and manage only their own content

- Public Users  
  Can view active content only

### Permission Design

Custom mixins enforce permissions at the view level:

- AdminRequiredMixin
- StaffRequiredMixin
- OwnershipRequiredMixin
- VisibilityQuerysetMixin

These mirror real-world authorization logic.

---

## Django REST Framework Layer (API)

The `api` app exposes REST APIs using DRF without affecting the HTML layer.

### DRF Concepts Implemented

- Serializer vs ModelSerializer
- Read vs write separation in serializers
- Nested serializers (read-only)
- ViewSets and Routers
- JWT authentication
- Permission classes
- Object-level permissions
- Filtering, searching, and ordering
- Pagination
- API versioning concepts
- Throttling and rate-limiting concepts
- Query optimization awareness

---

## Authentication

- Django sessions for HTML views
- JWT authentication for APIs

JWT is used to keep APIs stateless and production-ready.

Anonymous users:
- Read-only access where allowed

Authenticated users:
- Write access controlled by permissions

---

## Authorization & Permissions (API)

- `IsAuthenticated`
- `DjangoModelPermissions`
- Custom permission classes
- Object-level permission checks

Permission rules are consistent with the HTML layer:
- Admin: full access
- Staff: limited to owned resources
- Public: read-only

---

## Performance & Query Optimization

The project explicitly addresses common performance problems:

- N+1 query issues
- Serializer-caused extra queries
- Proper use of `select_related` and `prefetch_related`
- Pagination for large datasets
- Safe filtering and searching

Performance is treated as an engineering concern, not an afterthought.

---

## API Design Principles

- Predictable URLs
- Proper HTTP status codes
- Consistent error responses
- Clear separation of concerns
- Versioned API paths (e.g., `/api/v1/`)
- Secure defaults

---

## Running the Project Locally

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run migrations
5. Create a superuser
6. Start the development server

Example:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


---

## Learning Outcomes

This project demonstrates:

- How Django permissions scale in real systems
- How DRF differs from Django internally
- How authentication and authorization should be designed
- How to structure APIs professionally
- How to think about performance early
- How backend systems evolve beyond CRUD

---

## Author

Aashish Dangi  
Focus: Backend Engineering, Django, Django REST Framework
