from django.contrib import admin

from .models import (Street, AdjacentStreet, Sidewalk, SidewalkMap,
                     CommitIssue, SidewalkIssue,
                     SidewalkIssueBorder, Crosswalk, CrosswalkIssue,
                     CrosswalkBenefit, CrosswalkDirection)


class StreetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']


class AdjacentStreetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']


class SidewalkAdmin(admin.ModelAdmin):
    list_display = ['id', 'width_in_centimeters']
    search_fields = ['id']


class SidewalkMapAdmin(admin.ModelAdmin):
    ...


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']


class CommitIssueAdmin(admin.ModelAdmin):
    list_display = ['issue', 'status', 'date']
    list_filter = ['status', 'date']
    search_fields = ['issue']


class SidewalkIssueAdmin(admin.ModelAdmin):
    ...


class SidewalkIssueBorderAdmin(admin.ModelAdmin):
    list_display = ['height_in_centimeters', 'GPS']
    search_fields = ['GPS']


class CrosswalkAdmin(admin.ModelAdmin):
    list_display = ['type', 'width_in_centimeters']
    list_filter = ['type']
    search_fields = ['GPS']


class CrosswalkIssueAdmin(admin.ModelAdmin):
    list_display = ['border_height_in_centimeters']
    search_fields = ['border_height_in_centimeters']


class CrosswalkBenefitAdmin(admin.ModelAdmin):
    list_display = ['type']
    list_filter = ['type']


class CrosswalkDirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'direction']
    list_filter = ['direction']
    search_fields = ['name']


admin.site.register(Street, StreetAdmin)
admin.site.register(AdjacentStreet, AdjacentStreetAdmin)
admin.site.register(Sidewalk, SidewalkAdmin)
admin.site.register(SidewalkMap, SidewalkMapAdmin)
admin.site.register(CommitIssue, CommitIssueAdmin)
admin.site.register(SidewalkIssue, SidewalkIssueAdmin)
admin.site.register(SidewalkIssueBorder, SidewalkIssueBorderAdmin)
admin.site.register(Crosswalk, CrosswalkAdmin)
admin.site.register(CrosswalkIssue, CrosswalkIssueAdmin)
admin.site.register(CrosswalkBenefit, CrosswalkBenefitAdmin)
admin.site.register(CrosswalkDirection, CrosswalkDirectionAdmin)
