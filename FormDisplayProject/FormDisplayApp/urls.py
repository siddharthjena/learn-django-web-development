from django.urls import path
from . import views

urlpatterns = [
    path('view', views.Emp_reg_view)
]