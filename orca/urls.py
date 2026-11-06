from django.urls import path

from . import views

app_name = "orca"

urlpatterns = [
    path("", views.index, name="index"),
    path("tokens/", views.token_list, name="tokens"),
    path("icons/", views.icon_list, name="icons"),
    path("catalogue.json", views.catalogue_json, name="catalogue-json"),
    path("<slug:element_id>/", views.element, name="element"),
]
