from rest_framework.routers import DefaultRouter\n\nfrom apps.jobs.views import JobViewSet\n\nrouter = DefaultRouter()\nrouter.register(r'', JobViewSet, basename='job')\nurlpatterns = router.urls\n
