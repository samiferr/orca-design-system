from django.urls import path

from . import views

app_name = "orca"

urlpatterns = [
    path("", views.home, name="home"),
    path("primitives/", views.primitives, name="index"),
    path("components/", views.components, name="components"),
    path("patterns/", views.patterns, name="patterns"),
    path("guide/<slug:slug>/", views.guide, name="guide"),
    path("tokens/", views.token_list, name="tokens"),
    path("icons/", views.icon_list, name="icons"),
    path("catalogue.json", views.catalogue_json, name="catalogue-json"),
    path("<slug:element_id>/", views.element, name="element"),
]
