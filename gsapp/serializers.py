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


class UserMiniSerializer(serializers.ModelSerializer):
    """Вывод фамилии, имени и почты пользователя"""
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email')


class ReportsDetailSerializer(serializers.ModelSerializer):
    """Отчеты с подробной информацией"""
    report_type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    dept = serializers.SlugRelatedField(slug_field='name', read_only=True)
    submitter = UserMiniSerializer()
    assigned_user = UserMiniSerializer()
    added_users = UserMiniSerializer(many=True)
    subdept = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Reports
        fields = '__all__'
