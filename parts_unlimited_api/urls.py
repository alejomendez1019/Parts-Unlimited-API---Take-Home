from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from .swagger_settings import SWAGGER_SETTINGS

schema_view = get_schema_view(
   openapi.Info(
      title="Parts Unlimited API",
      default_version='v1',
      description="API documentation for the Parts Unlimited project",
      contact=openapi.Contact(email="alejomendez1019@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the parts app URL patterns
    path('api/', include('apps.parts.urls')),

    # API documentation URL patterns
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
