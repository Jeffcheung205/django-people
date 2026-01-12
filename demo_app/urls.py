# demo_app/urls.py
from django.urls import path
from .views import (
    LandingView,
    StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView, StudentCreateView,
    PeopleListView, PeopleDetailView, PeopleUpdateView, PeopleDeleteView,
)

app_name = "demo_app"

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),

    path("students/", StudentListView.as_view(), name="student"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),

    path("people/", PeopleListView.as_view(), name="people"),
    path("people/<int:pk>/", PeopleDetailView.as_view(), name="people-detail"),
    path("people/<int:pk>/update/", PeopleUpdateView.as_view(), name="people-update"),
    path("people/<int:pk>/delete/", PeopleDeleteView.as_view(), name="people-delete"),
]
