from django.contrib import admin

from blog.models import BlogPost, Author, Category


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ("slug", "date")
    # list_filter = ("author", "category")
    list_display = ("title", "author", "category", "date")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name",)
    list_display = ("full_name", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
