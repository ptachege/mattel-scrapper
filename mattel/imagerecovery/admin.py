from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ImageSourceLinks)
admin.site.register(Tire)
admin.site.register(Lego)
admin.site.register(HasbroToys)


@admin.register(AllProductLinks)
class AllProductLinks(admin.ModelAdmin):
    list_display = ("category_url", "crawled")


@admin.register(AgeCategories)
class AgeCategories(admin.ModelAdmin):
    list_display = ("category_url", "crawled")


# admin.site.register(ThemeCategories)
