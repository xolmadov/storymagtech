from django.contrib import admin
from .models import News, Gadget, Latest, Post

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

class GadgetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

class LatestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ('title', 'description')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author', 'descrepti')

admin.site.register(News, NewsAdmin)
admin.site.register(Gadget, GadgetAdmin)
admin.site.register(Latest, LatestAdmin)
admin.site.register(Post, PostAdmin)