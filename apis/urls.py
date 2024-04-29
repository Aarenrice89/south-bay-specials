from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from django.contrib.auth import views as auth_views

v1_router = routers.SimpleRouter()

v1_urlpatterns = [
    # # custom app urls
    # path("accounts/", include("django.contrib.auth.urls")),
    # drf-spectacular urls
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("specials/", include("specials.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

v1_urlpatterns += v1_router.urls

urlpatterns = [
    path("v1/", include(v1_urlpatterns)),
]