from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date_posted", "slug"]
    prepopulated_fields = {'slug': ('title',)}
