from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page
class AddAdmin(admin.ModelAdmin):
    list_display = ("title","category","url")
admin.site.register(Category)
admin.site.register(Page,AddAdmin)