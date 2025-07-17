from django.contrib import admin
from .models import Pizzashop, Category

class SpicyFilter(admin.SimpleListFilter):
    title = 'Выбор остроты'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('spicy', 'Острые'),
            ('not-spicy', 'Не острые'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'spicy':
            return queryset.filter(ostrota__isnull=False)
        elif self.value() == 'not-spicy':
            return queryset.filter(ostrota__isnull=True)


@admin.register(Pizzashop)
class PizzashopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    ordering = ['-time_create', 'title']
    actions = ['set_published']
    search_fields = ['title', 'cat__name']
    list_filter = [SpicyFilter, 'cat__name', 'is_published']

    def set_published(self, request, queryset):
        queryset.update(is_published=Pizzashop.Status.PUBLISHED)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')