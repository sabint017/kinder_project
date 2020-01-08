
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('home/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile, name='profile'),
    path('registerchild/', views.registerchild, name='registerchild'),
    path('attendance/', views.attendance, name='attendance'),
<<<<<<< HEAD
    path('food/', views.food, name='food'),
=======
    path('routine/', views.routine, name='routine'),
    path('addroutine/', views.addroutine, name='addroutine'),
>>>>>>> 9d6339d79500626496eef02e34ee9448514e376c
    path('addchild/', views.addchild, name='addchild'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
