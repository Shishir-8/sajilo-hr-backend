from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeCreateSerializer, EmployeeReadSerializer


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return EmployeeCreateSerializer
        return EmployeeReadSerializer