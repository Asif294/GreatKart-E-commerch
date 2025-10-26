from django.contrib import admin
from .import models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':( 'category',)}
    list_display =('category','slug')

admin.site.register(models.Category,CategoryAdmin)
