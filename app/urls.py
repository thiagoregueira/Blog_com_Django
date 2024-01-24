from django.urls import path
from app import views


app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path(
        "<int:day>/<int:month>/<int:year>/<slug:slug>/",
        views.post_detail,
        name="post_detail",
    ),
]
