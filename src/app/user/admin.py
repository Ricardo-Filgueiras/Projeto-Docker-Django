from django.contrib import admin
from django.contrib.auth.admin import User 
from .models import UserProfile


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active', 'date_joined')
    search_fields = ('username', 'email')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('username', 'email', 'first_name', 'last_name')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Datas Importantes', {
            'fields': ('date_joined', 'last_login'),
            'classes': ('collapse',)
        }),
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)