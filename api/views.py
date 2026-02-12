from rest_framework.viewsets import ModelViewSet
from content.models import Category, Content
from .serializers import CategorySerializer, ContentSerializer
from .querysets import ContentVisibilityMixin
from rest_framework.permissions import AllowAny
from .permissions import IsAuthenticatedOrReadOnly, IsOwnerOrStaff, IsStaffOrReadOnly


# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    
    
class ContentViewSet(ContentVisibilityMixin, ModelViewSet):
    queryset = Content.objects.select_related("category", "created_by")
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaff]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
