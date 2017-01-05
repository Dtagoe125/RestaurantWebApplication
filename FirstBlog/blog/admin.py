from django.contrib import admin
from models import Food, Menu

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Food, CategoryAdmin)
admin.site.register(Menu, CategoryAdmin)
