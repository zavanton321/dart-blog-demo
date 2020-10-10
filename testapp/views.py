from django.shortcuts import render


def demo_test(request):
    return render(request, 'testapp/test.html', context={'title': 'This is a test'})
