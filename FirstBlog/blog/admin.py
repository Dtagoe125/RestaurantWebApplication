from django.contrib import admin
from models import Food, Menu, Employee

#class CategoryAdmin(admin.ModelAdmin):
#	prepopulated_fields = {'slug':('name',)}

admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Employee)
