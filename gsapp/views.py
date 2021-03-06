from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.views import get_swagger_view
from .models import *
from rest_framework import viewsets, generics, permissions
from .serializers import *

schema_view = get_swagger_view(title='Pastebin API')


class ReportsAPIViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ReportsDetailSerializer
        else:
            return ReportsSerializer


class SubDeptsAPIViewSet(viewsets.ModelViewSet):
    queryset = SubDepts.objects.all()
    serializer_class = SubDeptsSerializer


class DeptsAPIViewSet(viewsets.ModelViewSet):
    queryset = Depts.objects.all()
    serializer_class = DeptsSerializer


class UsersAPIViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ReportTypesAPIViewSet(viewsets.ModelViewSet):
    queryset = ReportTypes.objects.all()
    serializer_class = ReportTypesSerializer


class FilesAPIViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer


class ConcernPermissionsAPIViewSet(viewsets.ModelViewSet):
    queryset = ConcernPermissions.objects.all()
    serializer_class = ConcernPermissionsSerializer

class DeptsTestView(generics.GenericAPIView):
    queryset = Depts
    serializer_class = DeptsSerializer
    permission_classes = [permissions.IsAuthenticated]