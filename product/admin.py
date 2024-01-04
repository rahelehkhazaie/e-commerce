from django.contrib import admin
from product.models import *
from . import models


admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Review)



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug' : ('title',)}
    