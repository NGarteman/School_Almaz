from .views import StudentModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"students", StudentModelViewSet, basename="students")
urlpatterns = router.urls