from django.urls import path
from project import views

app_name = 'sales'

urlpatterns = [
    path('', views.index, name='index')
]
