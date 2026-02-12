from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class AdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Admin Access Required")
        return super().dispatch(request, *args, **kwargs)


class StaffRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Staff Access Required")
        return super().dispatch(request, *args, **kwargs)


class OwnershipRequiredMixin(LoginRequiredMixin):
    owner_field = "created_by"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        owner = getattr(obj, self.owner_field, None)
        if self.request.user.is_staff:
            if owner == self.request.user:
                return obj
        raise PermissionDenied("You do not own this object")


class VisibilityQuerysetMixin(LoginRequiredMixin):
    def get_queryset(self):
        qs = super().get_queryset()

        user = self.request.user

        if user.is_staff:
            return qs

        return qs.filter(is_active=True)
