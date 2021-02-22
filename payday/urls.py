from django.urls import path
from . import views

app_name = 'payday'
urlpatterns = [
    path('', views.index, name = 'index')
]