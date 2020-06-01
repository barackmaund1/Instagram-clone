from django.contrib import admin
from .models import Image,Comment
# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('image', 'comment', 'pub_date','active')
    list_filter = ('active', 'pub_date')
    search_fields = ('comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)