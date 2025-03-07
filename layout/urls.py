from django.urls import path

from layout.views import home

urlpatterns = [
    path("", home, name="layout-home"),
]
