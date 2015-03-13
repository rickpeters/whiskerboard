from django.contrib import admin
from board.models import Category, Service, Status, Event


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Service, ServiceAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'severity')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Status, StatusAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('start', 'service', 'status', 'message')
    list_filter = ('service', 'status')

admin.site.register(Event, EventAdmin)
