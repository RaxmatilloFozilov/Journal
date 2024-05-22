from django.contrib import admin
from users.models import CustomUser, PasswordResets


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'birth_date', )
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    list_filter = ('birth_date',)
    ordering = ('email',)


class PasswordResetsAdmin(admin.ModelAdmin):
    list_display = ('user', 'reset_code', 'created_at', 'status')
    search_fields = ('user__email', 'reset_code')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PasswordResets, PasswordResetsAdmin)
