from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('book', viewsets.BookViewSet)

urlpatterns = router.urls
