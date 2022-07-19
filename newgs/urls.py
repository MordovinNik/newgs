"""newgs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from gsapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


reports_router = routers.SimpleRouter()
reports_router.register(r'reports', ReportsAPIViewSet)

depts_router = routers.SimpleRouter()
depts_router.register(r'depts', DeptsAPIViewSet)

subDepts_router = routers.SimpleRouter()
subDepts_router.register(r'subdepts', SubDeptsAPIViewSet)

usersRouter = routers.SimpleRouter()
usersRouter.register(r'users', UsersAPIViewSet)

reportTypes_router = routers.SimpleRouter()
reportTypes_router.register(r'report-types', ReportTypesAPIViewSet)

files_router = routers.SimpleRouter()
files_router.register(r'files', FilesAPIViewSet)

concern_permissions_router = routers.SimpleRouter()
concern_permissions_router.register(r'concern-permissions', ConcernPermissionsAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    url(r'swagger/', schema_view),
    path('api/v1/', include(reports_router.urls)),
    path('api/v1/', include(depts_router.urls)),
    path('api/v1/', include(subDepts_router.urls)),
    path('api/v1/', include(usersRouter.urls)),
    path('api/v1/', include(reportTypes_router.urls)),
    path('api/v1/', include(files_router.urls)),
    path('api/v1/', include(concern_permissions_router.urls)),
    path('api/v1/test-dept/', DeptsTestView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
