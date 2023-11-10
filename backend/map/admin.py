from django.contrib import admin
from .models import (Street, StreetType, AdjacentStreet, Sidewalk, SidewalkMap,
                     CommitIssue, IssueStatusType, SidewalkIssue,
                     SidewalkIssueBorder, Crosswalk, CrosswalkType, CrosswalkIssue,
                     CrosswalkBenefit, CrosswalkBenefitType, CrosswalkDirection, CrosswalkDirectionType)

# Street Admin
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']

# AdjacentStreet Admin
class AdjacentStreetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']
    search_fields = ['name']

# Sidewalk Admin
class SidewalkAdmin(admin.ModelAdmin):
    list_display = ['id', 'width_in_centimeters']
    search_fields = ['id']

# SidewalkMap Admin
class SidewalkMapAdmin(admin.ModelAdmin):
    ...
    # Customize as needed

# User Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']

# CommitIssue Admin
class CommitIssueAdmin(admin.ModelAdmin):
    list_display = ['issue', 'status', 'date']
    list_filter = ['status', 'date']
    search_fields = ['issue']

# SidewalkIssue Admin
class SidewalkIssueAdmin(admin.ModelAdmin):
    ...
    # Customize as needed

# SidewalkIssueBorder Admin
class SidewalkIssueBorderAdmin(admin.ModelAdmin):
    list_display = ['height_in_centimeters', 'GPS']
    search_fields = ['GPS']

# Crosswalk Admin
class CrosswalkAdmin(admin.ModelAdmin):
    list_display = ['type', 'width_in_centimeters']
    list_filter = ['type']
    search_fields = ['GPS']

# CrosswalkIssue Admin
class CrosswalkIssueAdmin(admin.ModelAdmin):
    list_display = ['border_height_in_centimeters']
    search_fields = ['border_height_in_centimeters']

# CrosswalkBenefit Admin
class CrosswalkBenefitAdmin(admin.ModelAdmin):
    list_display = ['type']
    list_filter = ['type']

# CrosswalkDirection Admin
class CrosswalkDirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'direction']
    list_filter = ['direction']
    search_fields = ['name']

# Register each model with its corresponding admin class
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
