from django.contrib import admin

from blog.models import BlogPost, Author, Category, BlogComment, Member


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ("slug", "date")
    # list_filter = ("author", "category")
    list_display = ("title", "author", "excerpt", "category", "date")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name",)
    list_display = ("user", "full_name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("excerpt",)
    list_display = ("author", "blog_post", "excerpt", "date",)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ("full_name",)
    list_display = ("user", "full_name",)
