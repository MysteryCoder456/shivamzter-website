from django.urls import path
from . import views

urlpatterns = [
    path("roadmaps/", views.get_roadmap_data),
]
