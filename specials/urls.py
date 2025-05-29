from django.conf import settings
from django.urls import path
from rest_framework import routers

from apis.constants import PRODUCTION
from specials import views

router = routers.SimpleRouter()
router.register("", views.SpecialViewset, basename="")

app_name = "specials"

urlpatterns = [
    path("grouped/", views.ListGroupedSpecialsView.as_view(), name="grouped"),
]
if settings.ENVIRONMENT != PRODUCTION:
    urlpatterns.append(
        path("export/", views.ExportSpecialsToCSV.as_view(), name="export"),
    )
urlpatterns += router.urls
