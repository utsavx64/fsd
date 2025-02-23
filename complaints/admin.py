from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('name', 'email', 'product', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
