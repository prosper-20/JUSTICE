from django.urls import path
from .views import api_home_view, api_detail_view, api_update_view, api_delete_view, api_create_view, api_registration_view


urlpatterns = [
    path("home", api_home_view, name="home2"),
    path("<slug:slug>/", api_detail_view, name="detail2"),
    path("<slug:slug>/update", api_update_view, name="update"),
    path("<slug:slug>/delete", api_delete_view, name="delete"),
    path("create", api_create_view, name="create"),
    path("register", api_registration_view, name="register")
] 