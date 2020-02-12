
from .views import PostDetailView, addresult, ResultDetail, ResultUpdate, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, RoutineDetailView, RoutineListView, RoutineUpdateView, NoticeCreateView, NoticeDeleteView, NoticeDetailView, NoticeUpdateView, AttendanceDetailView, present, absent
from . import views
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('home/', views.postsandnotices, name='home'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('notice/<slug>/', NoticeDetailView.as_view(), name='notice-detail'),
    path('notice/new/', NoticeCreateView.as_view(), name='notice-create'),
    path('notice/<int:pk>/update', NoticeUpdateView.as_view(), name='notice-update'),
    path('notice/<int:pk>/delete', NoticeDeleteView.as_view(), name='notice-delete'),


    path('profile/', views.profile, name='profile'),
    path('registerchild/', views.registerchild, name='registerchild'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/<int:pk>', AttendanceDetailView.as_view(),
         name='attendance-detail'),
    path('food/', views.food, name='food'),
    path('addfood/', views.addfood, name='add_food'),
    path('routine/', RoutineListView.as_view(), name='routine'),
    path('addroutine/', views.addroutine, name='addroutine'),
    path('addchild/', views.addchild, name='addchild'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('routine/<int:pk>/', RoutineDetailView.as_view(), name='routine-detail'),
    path('routine/<int:pk>/update',
         RoutineUpdateView.as_view(), name='routine-update'),
    path('result/', views.result, name='result'),
    path('addresult/', views.addresult, name='addresult'),
    path('present/<id>/', present, name="present"),
    path('absent/<id>/', absent, name="absent"),
    path('result/<int:pk>/update', ResultUpdate.as_view(), name='result-update'),
    path('result/<int:pk>/', ResultDetail.as_view(), name='result-detail'),

]
