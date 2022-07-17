from rest_framework import serializers

from .models import *


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


class SubDeptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepts
        fields = '__all__'


class DeptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depts
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ReportTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportTypes
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class ConcernPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcernPermissions
        fields = '__all__'

