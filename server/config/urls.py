"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from api.views import FacultyView, InboxView, LetterView, RemarkView, StudentView, UserView, MeView

schema_view = get_schema_view(
    openapi.Info(
        title="OAPS API",
        default_version='v1',
        description="OAPS API documentation",
        terms_of_service="oaps/terms",
        contact=openapi.Contact(email="admin@oaps.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('user/<int:user_id>', UserView.as_view()),
    path('letter/<int:letter_id>', LetterView.as_view()),
    path('me/', MeView.as_view()),
    path('faculty/<int:fac_id>', FacultyView.as_view()),
    path('inbox/<int:user_id>', InboxView.as_view()),
    path('remark/<int:remark_id>', RemarkView.as_view()),
    path('student/<int:std_id>', StudentView.as_view()),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
]
