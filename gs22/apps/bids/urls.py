from rest_framework.routers import DefaultRouter\n\nfrom apps.bids.views import BidViewSet\n\nrouter = DefaultRouter()\nrouter.register(r'', BidViewSet, basename='bid')\nurlpatterns = router.urls\n
