from django.urls import path

from blog.views import get_category, Home, demo_post

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', demo_post, name='post'),
]
