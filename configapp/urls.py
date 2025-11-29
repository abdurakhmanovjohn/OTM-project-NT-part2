from django.urls import path
from .views import *

app_name = "configapp"

urlpatterns = [
    # path("", views.index, name="index"),

    # path("otm/", views.otm_list, name="otm_list"),
    # path("otm/add/", views.otm_add, name="otm_create"),
    # path("otm/edit/<int:pk>/", views.otm_edit, name="otm_edit"),
    # path("otm/delete/<int:pk>/", views.otm_delete, name="otm_delete"),

    # path("groups/", views.group_list, name="group_list"),
    # path("groups/add/", views.group_add, name="group_create"),
    # path("groups/edit/<int:pk>/", views.group_edit, name="group_edit"),
    # path("groups/delete/<int:pk>/", views.group_delete, name="group_delete"),

    # path("students/", views.student_list, name="student_list"),
    # path("students/add/", views.student_add, name="student_create"),
    # path("students/edit/<int:pk>/", views.student_edit, name="student_edit"),
    # path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),
    # path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path("", IndexView.as_view(), name="index"),

    path("otm/", OTMListView.as_view(), name="otm_list"),
    path("otm/add/", OTMCreateView.as_view(), name="otm_create"),
    path("otm/edit/<int:pk>/", OTMUpdateView.as_view(), name="otm_edit"),
    path("otm/delete/<int:pk>/", OTMDeleteView.as_view(), name="otm_delete"),

    path("groups/", GroupListView.as_view(), name="group_list"),
    path("groups/add/", GroupCreateView.as_view(), name="group_create"),
    path("groups/edit/<int:pk>/", GroupUpdateView.as_view(), name="group_edit"),
    path("groups/delete/<int:pk>/", GroupDeleteView.as_view(), name="group_delete"),

    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/add/", StudentCreateView.as_view(), name="student_create"),
    path("students/edit/<int:pk>/", StudentUpdateView.as_view(), name="student_edit"),
    path("students/delete/<int:pk>/", StudentDeleteView.as_view(), name="student_delete"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
]