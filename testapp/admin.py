from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from testapp.models import Rubric, Article

admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(Article)
