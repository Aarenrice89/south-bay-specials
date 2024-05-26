from rest_framework import routers
from specials import views

router = routers.SimpleRouter()
router.register("", views.SpecialViewset, basename="")

app_name = "specials"

urlpatterns = []
urlpatterns += router.urls
