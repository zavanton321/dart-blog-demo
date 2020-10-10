from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', context={'name': 'zavanton'})


def get_category(request, slug):
    return render(request, 'blog/category.html', context={'the_slug': slug})
