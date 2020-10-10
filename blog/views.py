from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class Home(ListView):
    context_object_name = 'posts'
    paginate_by = 4
    model = Post
    template_name = 'blog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Classic Blog Design'
        return context


def index(request):
    return render(request, 'blog/index.html', context={'name': 'zavanton'})


def get_category(request, slug):
    return render(request, 'blog/category.html', context={'the_slug': slug})


def demo_post(request, slug):
    return HttpResponse(f"Post slug: {slug}")
