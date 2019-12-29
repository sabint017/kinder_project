from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from users import views as users_views
urlpatterns = [
    path('', views.index, name='index'),

    path('home/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('dev.html', views.dev, name='dev'),
    path('queries.html', views.queries, name='queries'),
    path('services.html', views.services, name='services'),
    path('register_parent.html', users_views.register_parent, name="register_parent"),
    path('register_teacher.html', users_views.register_teacher, name="register_teacher"),
    path('signup.html', views.signup, name='signup'),
]
