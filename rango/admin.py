from django.contrib import admin

# Register your models here.
from rango.models import UserProfile
from django.contrib import admin
from rango.models import Category, Page
class AddAdmin(admin.ModelAdmin):
    list_display = ("title","category","url")

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,AddAdmin)
admin.site.register(UserProfile)