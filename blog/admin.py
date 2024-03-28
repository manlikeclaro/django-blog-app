from django.contrib import admin

from blog.models import BlogPost, Author


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("author",)
    list_display = ("title", "author")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name",)
    list_display = ("full_name",)
