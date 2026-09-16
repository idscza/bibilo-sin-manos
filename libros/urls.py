from rest_framework.routers import DefaultRouter
from .views import LibroViewSet


router = DefaultRouter()

router.register(r'libros', LibroViewSet)

urlpatterns = router.urls


"""
from django.urls import path
from .views import LibroListView

urlpatterns = [
    path('libros/', LibroListView.as_view(), name='libro-list'),
]"""