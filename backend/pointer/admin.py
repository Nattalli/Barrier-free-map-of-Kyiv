from django.contrib import admin
from .models import MapPoint, Addition, MapPointCategory

class AdditionAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']


class MapPointAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'is_approved']
    list_filter = ['is_approved', 'addition', 'title']
    search_fields = ['title', 'address']
    filter_horizontal = ('addition',)


admin.site.register(MapPoint, MapPointAdmin)
admin.site.register(Addition, AdditionAdmin)
admin.site.register(MapPointCategory)
