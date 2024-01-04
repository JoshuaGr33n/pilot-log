#pilot_log/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModelViewSet


router = DefaultRouter()
router.register(r'', ModelViewSet, basename='')


urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += [
    path('import/', ModelViewSet.as_view({'post': 'create'}), name='import'),
    path('export/', ModelViewSet.as_view({'get': 'list'}), name='export'),
]
