from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

from users import views as users_views
urlpatterns = [
    path('', views.index, name='index'),

    path('home/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('dev.html', views.dev, name='dev'),
    path('queries.html', views.queries, name='queries'),
    path('services.html', views.services, name='services'),
    path('register.html', users_views.register, name="register"),
]
