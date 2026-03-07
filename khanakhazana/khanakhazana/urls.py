
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include the URLs from the core app
    path('about/', include('core.urls')),  # Include the URLs from the core app for about page
    path('footer/', include('core.urls')),
]
