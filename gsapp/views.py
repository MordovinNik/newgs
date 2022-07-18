from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.views import get_swagger_view
from .models import *
from rest_framework import viewsets
from .serializers import *

schema_view = get_swagger_view(title='Pastebin API')


class ReportsAPIViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

    def list(self, request, *args, **kwargs):
        reports = Reports.objects.all()
        serializer = ReportsDetailSerializer(reports, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        reports = Reports.objects.all()
        serializer = ReportsDetailSerializer(reports)
        return Response(serializer.data)


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