from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('post/create', views.postCreate, name='postCreate'),
    path('post/<int:post_id>', views.postView, name='postView'),
    path('post/update/<int:post_id>', views.postUpdate, name='postUpdate'),
    path('post/delete/<int:post_id>', views.postDelete, name='postDelete'),
]
