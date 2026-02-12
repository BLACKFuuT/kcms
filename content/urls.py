from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryUpdateView,
    CategoryListView,
)
from .views import (
    ContentCreateView,
    ContentDeleteView,
    ContentDetailView,
    ContentListView,
    ContentUpdateView,
)
from .views import StaffCreateView, StaffListView, SignUpView

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="categories-list"),
    path("categories/create/", CategoryCreateView.as_view(), name="categories-create"),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="categories-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="categories-delete",
    ),
    path("content/", ContentListView.as_view(), name="content-list"),
    path("content/<int:pk>/", ContentDetailView.as_view(), name="content-detail"),
    path("content/create/", ContentCreateView.as_view(), name="content-create"),
    path(
        "content/<int:pk>/update/", ContentUpdateView.as_view(), name="content-update"
    ),
    path(
        "content/<int:pk>/delete/", ContentDeleteView.as_view(), name="content-delete"
    ),
    path("staff/create/", StaffCreateView.as_view(), name="staff-create"),
    path("staff/", StaffListView.as_view(), name="staff-list"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
