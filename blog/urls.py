from django.urls import path

from blog.views import Home, demo_post, PostsByCategory

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', demo_post, name='post'),
]
