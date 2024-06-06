from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the parts app URL patterns
    path('api/', include('apps.parts.urls')),
]
