from django.contrib import admin
from .models import HomePage, Page, Social, Contact
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title_Text', 'Category')
    search_fields = ('Title',)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Social_Media', 'Social_Media_Link')
    search_fields = ('Social_Media',)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Email', 'Phone_Number', 'Position')
    search_fields = ('Name','Email','Position')
admin.site.register(HomePage)
admin.site.register(Page, PageAdmin)
admin.site.register(Social, SocialsAdmin) 
admin.site.register(Contact, ContactsAdmin) 