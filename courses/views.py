from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializers


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
