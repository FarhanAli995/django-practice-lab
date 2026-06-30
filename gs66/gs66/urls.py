
# Root URL config — includes app-level routes
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('root.urls')),  # delegate to our app
]