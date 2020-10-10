from django.http import HttpResponse
from django.views.generic import ListView

from blog.models import Post, Category


class Home(ListView):
    context_object_name = 'posts'
    paginate_by = 4
    model = Post
    template_name = 'blog/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostsByCategory(ListView):
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/index.html'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


def demo_post(request, slug):
    return HttpResponse(f"Post slug: {slug}")
