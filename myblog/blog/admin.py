from django.contrib import admin
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    # pass
    list_display = ('tilte','content','pub_time')
    list_filter = ('pub_time',)
admin.site.register(Article,ArticleAdmin)