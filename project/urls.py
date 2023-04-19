from django.contrib import admin
from django.urls import path, include  # new

# new
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  # new
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path("articles/", include("articles.urls")),
    path("", include("pages.urls")),
]
