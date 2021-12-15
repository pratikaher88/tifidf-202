from django.urls import include, re_path, path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.main_frontend, name="index"),
    path('', views.main_frontend, name="generate"),
    path('export', views.export_to_csv, name="export_to_csv"),
    path('search', views.search, name="search"),
    re_path(r'^ajax/get_response/$', views.search_ajax, name='get_response')

]