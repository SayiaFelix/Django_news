from django.contrib import admin
from .models import Editor,Article,tags,NewsLetterRecipients

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(NewsLetterRecipients)