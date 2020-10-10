from django.db.models import F
from django.views.generic import ListView, DetailView

from blog.models import Post, Category, Tag


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
    paginate_by = 4
    template_name = 'blog/index.html'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/index.html'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug__contains=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Записи по тэгу ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class GetPost(DetailView):
    context_object_name = 'post'
    model = Post
    template_name = 'blog/single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Post.objects.get(slug=self.kwargs['slug'])
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    paginate_by = 4
    context_object_name = "posts"
    template_name = 'blog/search.html'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Результаты поиска'
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
