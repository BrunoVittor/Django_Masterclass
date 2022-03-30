from django.contrib import admin
from .models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'fone', 'email']
	list_display_links = ['name', 'fone', 'email']
	search_fields = ['name', 'fone', 'email']
	list_filter = ['name']


admin.site.register(Contact, ContactAdmin)
