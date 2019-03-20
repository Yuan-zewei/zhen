from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post_list, name='post_list'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='update'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
]
