
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RoutineUpdateView, RoutineDetailView, RoutineListView
from . import views
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('home/', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('routine/<int:pk>/',
         RoutineDetailView.as_view(), name='routine-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('routine/<int:pk>/update',
         RoutineUpdateView.as_view(), name='routine-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('profile/', views.profile, name='profile'),
    path('registerchild/', views.registerchild, name='registerchild'),
    path('attendance/', views.attendance, name='attendance'),
    path('routine/', RoutineListView.as_view(), name='routine'),
    path('addroutine/', views.addroutine, name='addroutine'),
    path('addchild/', views.addchild, name='addchild'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
