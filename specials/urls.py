from django.urls import path
from specials import views

app_name="specials"

urlpatterns = [
    path("ping/", views.ping, name="test"),
]
