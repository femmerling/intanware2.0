from page.models import Page, MediaFile, DocumentFile, CssFile
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Page Identification', {'fields': ['page_id','page_name'],}),
        ('Page Metadata', {'fields': ['page_title','page_key','page_desc']}),
        ('Page Content', {'fields': ['page_content','page_status']}),
    ]
    list_display = ('page_id','page_name', 'page_key','page_desc')
    search_fields = ['page_key']

class MediaFileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image File', {'fields': ['file'],}),
    ]
    list_filter = ['created']
  
class DocumentFileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Document File', {'fields': ['file'],}),
    ]
    list_filter = ['created']
    
class CssFileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Stylesheet File', {'fields': ['file'],}),
    ]
    list_filter = ['created']
    
admin.site.register(Page, PageAdmin)
admin.site.register(MediaFile, MediaFileAdmin)
admin.site.register(DocumentFile, DocumentFileAdmin)
admin.site.register(CssFile, CssFileAdmin)