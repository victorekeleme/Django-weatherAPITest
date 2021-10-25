from django.urls import path
from . import views


urlpatterns = [
    # url path to page
    path('', views.api_display, name= 'weather_list'),
]