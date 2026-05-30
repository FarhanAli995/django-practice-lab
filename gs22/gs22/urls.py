from django.contrib import admin\nfrom django.urls import include, path\n\nurlpatterns = [\n    path('admin/', admin.site.urls),\n    path('api/auth/register/', include('apps.users.urls')),\n]\n
