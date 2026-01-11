from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journal.views import PaperViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'papers', PaperViewSet, basename='papers')
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
