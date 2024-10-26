from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from apis import views as api_views

v1_router = routers.SimpleRouter()

v1_urlpatterns = [
    # drf-spectacular urls
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # custom app urls
    path("specials/", include("specials.urls")),
    path("locations/", include("locations.urls")),
    path("ping/", api_views.ping, name="ping"),
]

v1_urlpatterns += v1_router.urls

urlpatterns = [
    path("v1/", include(v1_urlpatterns)),
]
