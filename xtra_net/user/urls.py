from django.urls import path
from . import views

urlpatterns = [
    path('', views.use_Home, name='use_Home'),
    path('submit_data', views.submit_data, name='submit_data'),
]