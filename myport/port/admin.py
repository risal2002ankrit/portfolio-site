from django.contrib import admin
from .models import category, Article, Resume, Blog, Yourself

# Register your models here.
admin.site.register(Yourself)
admin.site.register(category)
admin.site.register(Article)
admin.site.register(Resume)
admin.site.register(Blog)


