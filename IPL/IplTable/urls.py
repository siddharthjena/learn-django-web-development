from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.retrive_data),
]