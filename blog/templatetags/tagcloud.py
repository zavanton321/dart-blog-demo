from django import template

from blog.models import Tag

register = template.Library()


@register.inclusion_tag('blog/tag_cloud_tpl.html')
def get_tag_cloud(max_num=100):
    tags = Tag.objects.all()[:max_num]
    return {'tags': tags}
