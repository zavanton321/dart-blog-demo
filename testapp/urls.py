from django.urls import path

from testapp.views import demo_test, get_rubric

urlpatterns = [
    path('', demo_test, name='test'),
    path('rubric/<int:pk>', get_rubric, name='rubric'),
]
