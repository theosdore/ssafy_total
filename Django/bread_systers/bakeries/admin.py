from django.contrib import admin

# Register your models here.
from .models import Bakery

# admin.site.register(Bakery)
@admin.register(Bakery)
class BakeryAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "rating")