from django.contrib import admin
from .models import BugReport, FeatureRequest
from django.contrib.admin.actions import action


@action(description='Set status on Complete of selected bugs')
def mark_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title', 'description') 
    list_editable = ('status', 'priority')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Info', {
            'fields': ('project', 'task', 'status', 'priority')
        })
    )
    actions = [mark_completed]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('title', 'description') 
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Info', {
            'fields': ('project', 'task', 'status', 'priority')
        })
    )