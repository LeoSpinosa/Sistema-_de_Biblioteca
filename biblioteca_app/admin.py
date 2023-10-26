from django.contrib import admin
from .models import Gender, Books

class BooksAdmin(admin.ModelAdmin):

    list_display = ['name', 'gender', 'qtd_pages']
    search_fields = ['name']

admin.site.register(Books, BooksAdmin)
admin.site.register(Gender)

