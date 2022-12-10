from .views import PostListView, PostDetailView
from django.urls import path


urlpatterns =[
    path("", PostListView.as_view(), name="home"),
    path("<slug:slug>/", PostDetailView.as_view(), name="detail")
]