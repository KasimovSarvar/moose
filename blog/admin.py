from django.contrib import admin
from .models import Post, Category, Comment, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'is_solved', 'created_at')
    list_display_links = ('id', 'full_name')
    list_editable = ('is_solved',)
    list_filter = ('created_at', 'is_solved')


    class Meta:
        model = Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_name', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('created_at', 'author_name')

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact, ContactAdmin)