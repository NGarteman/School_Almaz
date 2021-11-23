from .views import CourseModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"courses", CourseModelViewSet, basename="courses")
urlpatterns = router.urls