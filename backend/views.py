from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Nexus Backend!")
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the ALX E-Commerce API",
        "docs": {
            "swagger": "/api/schema/swagger/",
            "redoc": "/api/schema/redoc/",
        }
    })
