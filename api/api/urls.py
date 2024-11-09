"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from post import urls as post_urls

urls = [
    path(
        "v1/",
        include(
            [
                path(
                    "schema/",
                    SpectacularAPIView.as_view(api_version="v1"),
                    name="v1-schema",
                ),
                path(
                    "schema/swagger-ui/",
                    SpectacularSwaggerView.as_view(url_name="v1-schema"),
                    name="swagger-ui",
                ),
                path(
                    "schema/redoc/",
                    SpectacularRedocView.as_view(url_name="v1-schema"),
                    name="redoc",
                ),
                path(
                    "post/",
                    include((post_urls, "post")),
                    name="post",
                ),
            ]
        ),
    )
]

urlpatterns = [
    path("admin/", admin.site.urls),
] + urls
