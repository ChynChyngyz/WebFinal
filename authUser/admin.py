from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'nickname', 'role', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nickname')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация',
         {'fields': ('first_name', 'last_name', 'nickname', 'phone', 'date_of_birth', 'avatar')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        ('Даты', {'fields': ('date_joined',)}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj and obj.role == 'Doctor':
            doctor_fieldset = ('Информация о докторе',
                               {'fields': ('speciality', 'description', 'experience', 'education')})
            fieldsets = fieldsets + (doctor_fieldset,)
        return fieldsets

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Персональная информация',
         {'fields': ('first_name', 'last_name', 'nickname', 'phone', 'date_of_birth', 'avatar')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
    )

    # filter_horizontal = ('doctor_time_work')
    list_editable = ('is_active', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
