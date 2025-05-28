from django.urls import path
from rest_framework import routers

from specials import views

router = routers.SimpleRouter()
router.register("", views.SpecialViewset, basename="")

app_name = "specials"

urlpatterns = [
    path("grouped/", views.ListGroupedSpecialsView.as_view(), name="grouped"),
]
urlpatterns += router.urls
