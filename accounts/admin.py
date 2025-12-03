from django.contrib import admin
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Nexus Admin"
    site_title = "Nexus Admin Portal"
    index_title = "Welcome, Abdullahi"
    
    # Add custom CSS
    def each_context(self, request):
        context = super().each_context(request)
        context['custom_admin_css'] = 'admin_custom/custom.css'
        return context

admin_site = MyAdminSite(name='myadmin')

# Example: registering models
# from .models import User, Group
# admin_site.register(User)
# admin_site.register(Group)
