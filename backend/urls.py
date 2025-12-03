# backend/urls.py
from django.contrib import admin    
from django.urls import path, include
from django.http import JsonResponse

def root(request):
    return JsonResponse({"message": "Welcome to ALX Nexus API"})

urlpatterns = [
    path("", root),
    path('admin/', admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/products/", include("catalog.urls")),
]
