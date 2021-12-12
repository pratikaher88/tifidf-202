from django.urls import include, re_path, path
from . import views

app_name = 'frontend'

urlpatterns = [
    re_path('', views.main_frontend, name="index"),
    re_path('', views.main_frontend, name="generate"),
    path('export/', views.export_users_csv, name="export_to_csv")
]