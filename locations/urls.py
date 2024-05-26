from locations import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("", views.LocationViewSet, basename="")

app_name = "locations"

urlpatterns = []
urlpatterns += router.urls
