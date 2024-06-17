from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save(using='users_db')
        
    def delete_model(self, request, obj):
        obj.delete(using='users_db')
        
    def get_queryset(self, request):
        return super().get_queryset(request).using('users_db')
    

admin.site.register(User, UserAdmin)