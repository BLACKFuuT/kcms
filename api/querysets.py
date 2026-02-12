from content.models import Content

class ContentVisibilityMixin:
    def get_queryset(self):
        qs = Content.objects.select_related("category", "created_by" )

        user = self.request.user

        if user.is_authenticated and user.is_staff:
            return qs

        return qs.filter(is_active=True)

