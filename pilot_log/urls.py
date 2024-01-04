#pilot_log/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YourModelViewSet


router = DefaultRouter()
router.register(r'', YourModelViewSet, basename='')


urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += [
    path('import/', YourModelViewSet.as_view({'post': 'create'}), name='import'),
    path('export/', YourModelViewSet.as_view({'get': 'list'}), name='export'),
]
