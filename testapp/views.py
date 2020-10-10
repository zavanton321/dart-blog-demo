from django.http import HttpResponse
from django.shortcuts import render

from testapp.models import Rubric


def demo_test(request):
    return render(request, 'testapp/test.html', {'rubrics': Rubric.objects.all()})


def get_rubric(request, pk):
    return HttpResponse(f"Rubric: {pk}")
