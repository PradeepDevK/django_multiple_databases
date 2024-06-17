from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save(using='books_db')
        
    def delete_model(self, request, obj):
        obj.delete(using='books_db')
        
    def get_queryset(self, request):
        return super().get_queryset(request).using('books_db')
    
    
admin.site.register(Book, BookAdmin)