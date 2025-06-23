# Django Library Management System

This is a **Library Management System** built with Django.
Add, update, delete, and view book records
View book details
Bootstrap styling with custom CSS
Class-based views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)
Static file handling
Template inheritance with `base.html`

library/`: Main app (models, views, forms)
`Library_management/`: Django project settings and URLs
`templates/library/`: HTML files
`static/css/`: Custom CSS (e.g., `index.css`)
`manage.py`: Django management script

 How to Run
# Step 1: Install dependencies
pip install django

# Step 2: Run migrations
python manage.py makemigrations
python manage.py migrate

# Step 3: Run the server
python manage.py runserver
