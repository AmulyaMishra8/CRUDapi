from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializers

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers