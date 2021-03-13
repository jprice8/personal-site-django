from django.urls import path

from . import views

urlpatterns = [
    # django template routing. NOT API ROUTING.
    path('', views.PostList.as_view(), name='post-list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('<hashtag>/', views.filter_hashtag, name='post-hashtag'),
]