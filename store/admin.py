from django.contrib import admin

from . import models

class AdminBase(admin.ModelAdmin):
    ordering = ('-updated_at',)
    readonly_fields=('created_at', 'updated_at', 'key', 'id', )

# Register your models here.
@admin.register(models.Companies)
class CompaniesAdmin(AdminBase):
    pass

@admin.register(models.Categories)
class CategoriesAdmin(AdminBase):
    pass

@admin.register(models.Products)
class ProductsAdmin(AdminBase):
    pass
