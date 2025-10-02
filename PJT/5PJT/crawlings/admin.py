from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ("id",  'nickname', 'content', 'post_time', 'ttabong', 'ZZal', 'company_name', 'company_code')

# @admin.register(Analyst)
# class AnalystAdmin(admin.ModelAdmin):
#   list_display = ("id", 'company_name', 'context_analyst', 'save_data')