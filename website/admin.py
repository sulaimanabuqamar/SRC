from django.contrib import admin
from .models import HomePage, Page
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title_Text', 'Category')
    search_fields = ('Title',)
admin.site.register(HomePage)
admin.site.register(Page, PageAdmin)