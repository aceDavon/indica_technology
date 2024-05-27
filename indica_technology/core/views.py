from rest_framework import generics, status
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({"data": serializer.data, "status": status.HTTP_200_OK})
