from django.urls import path
from . import views

urlpatterns = [
    path('view', views.redg_view),
]
