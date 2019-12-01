from . import views
from django.urls import path
from users import views as users_views
urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.home, name='home'),

    path('dev.html', views.dev, name='dev'),
    path('queries.html', views.queries, name='queries'),
    path('services.html', views.services, name='services'),
    path('register.html', users_views.register, name="register"),
]
