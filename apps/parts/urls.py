from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartViewSet
from apps.parts.views import common_words

router = DefaultRouter()
router.register(r'parts', PartViewSet)

urlpatterns = [
    # Include all routes defined in the router
    path('', include(router.urls)),
    path('common-words/', common_words, name='common-words')
]
