from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ContentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("contents", ContentViewSet, basename="contents")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    
]
