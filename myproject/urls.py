from django.contrib import admin
from django.urls import path, include

urlpatterns = [  # Admin panel route
    path("", include("myapp.urls")),  # Delegate API-related routes to the app
]
