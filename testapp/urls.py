from django.urls import path

from testapp.views import demo_test

urlpatterns = [
    path('', demo_test, name='test'),
]