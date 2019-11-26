from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='app1-home'),

]
