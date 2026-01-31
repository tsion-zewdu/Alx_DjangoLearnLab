# Library Project – Advanced Features and Security

## Description
This Django project demonstrates advanced features including model relationships, custom permissions, user groups, and view protection.

## Features
- Book, Author, and Library models
- Custom permissions (view, create, edit)
- Role-based access control using Django groups
- Protected views using @permission_required

## User Roles
- **Admins**: Full permissions
- **Editors**: Can create and edit books
- **Viewers**: Can view books only

## Technologies Used
- Python
- Django
- SQLite

## How to Run
1. Clone the repository
2. Install dependencies
3. Run migrations
4. Start the server

```bash
python manage.py migrate
python manage.py runserver
