from rest_framework import routers

from locations import views

router = routers.SimpleRouter()
router.register("", views.LocationViewSet, basename="")

app_name = "locations"

urlpatterns = []
urlpatterns += router.urls
