## User Authentication System

This project implements a complete user authentication system using Django.

### Features
- User registration with username, email, and password
- Secure login and logout
- User profile viewing and editing
- CSRF protection on all forms
- Password hashing using Django's built-in security

### How to Test
1. Run the server:
   python manage.py runserver
2. Register a user at /register
3. Login at /login
4. View and update profile at /profile
5. Logout at /logout

## Comment System

Users can:
- View comments under each blog post
- Add comments (authenticated users only)
- Edit or delete their own comments

Permissions:
- Only the comment author can edit or delete a comment.
- Unauthenticated users can only read comments.
