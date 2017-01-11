from django.contrib import admin
from articles.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
admin.site.register(Article, ArticleAdmin)