from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_data, name='save_data')
]