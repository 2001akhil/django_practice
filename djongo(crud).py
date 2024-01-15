# Install Djongo
# pip install djongo

# Configure Djongo in settings.py
# settings.py
# DATABASES = {'default': {'ENGINE': 'djongo','NAME': 'your_db_name',}}

# Define Models
# models.py
# from djongo import models
# class User(models.Model): username = models.CharField(max_length=255) email = models.EmailField()

# Perform CRUD Operations
# views.py
# from django.shortcuts import render
# from .models import User

# Create (Insert) Operation
# def create_user(request): user_data = {'username': 'john_doe', 'email': 'john@example.com'} new_user = User.objects.create(**user_data) return render(request, 'success.html', {'message': 'User created successfully'})

# Read Operation
# def read_user(request, user_id): user = User.objects.get(pk=user_id) return render(request, 'user_detail.html', {'user': user})

# Update Operation
# def update_user(request, user_id): user = User.objects.get(pk=user_id) user.email = 'new_email@example.com' user.save() return render(request, 'success.html', {'message': 'User updated successfully'})

# Delete Operation
# def delete_user(request, user_id): user = User.objects.get(pk=user_id) user.delete() return render(request, 'success.html', {'message': 'User deleted successfully'})
