from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializers


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers



