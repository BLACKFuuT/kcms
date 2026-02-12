from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from CMS.mixins import (
    AdminRequiredMixin,
    StaffRequiredMixin,
    OwnershipRequiredMixin,
    VisibilityQuerysetMixin,
)
from .models import User, Category, Content
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

# Create your views here.


class CategoryListView(ListView):
    model = Category
    template_name = "content/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    fields = ["name", "description", "is_active"]
    template_name = "content/category_form.html"
    success_url = reverse_lazy("categories-list")


class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Category
    fields = ["name", "description", "is_active"]
    template_name = "content/category_form.html"
    success_url = reverse_lazy("categories-list")


class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    model = Category
    template_name = "content/category_confirm_delete.html"
    success_url = reverse_lazy("category-list")


# Content


class ContentListView(VisibilityQuerysetMixin, ListView):
    model = Content
    template_name = "content/content_list.html"
    context_object_name = "contents"
    paginate_by = 5

    def get_queryset(self):
        return Content.objects.filter(is_active=True).select_related(
            "category", "created_by"
        )


class ContentDetailView(VisibilityQuerysetMixin, DetailView):
    model = Content
    template_name = "content/content_detail.html"


class ContentCreateView(StaffRequiredMixin, SuccessMessageMixin, CreateView):
    model = Content
    fields = ["category", "title", "body", "image", "is_active"]
    template_name = "content/content_form.html"
    success_url = reverse_lazy("content-list")
    success_message = "Content Created Successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ContentUpdateView(OwnershipRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Content
    fields = ["category", "title", "body", "image", "is_active"]
    template_name = "content/content_form.html"
    success_url = reverse_lazy("content-list")
    success_message = "Content Updated Successfully"


class ContentDeleteView(OwnershipRequiredMixin, DeleteView):
    model = Content
    template_name = "content/content_confirm_delete.html"
    success_url = reverse_lazy("content-list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Content deleted successfully 🗑️")
        return super().delete(request, *args, **kwargs)


class StaffCreateView(AdminRequiredMixin, CreateView):
    model = User
    fields = ["username", "email", "is_staff", "password"]
    template_name = "content/staff_form.html"
    success_url = reverse_lazy("staff-list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        password = form.cleaned_data.get("password")
        self.object.set_password(password)
        self.object.save()
        return super().form_valid(form)


class StaffListView(AdminRequiredMixin, ListView):
    model = User
    template_name = "content/staff_list.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy("login")


