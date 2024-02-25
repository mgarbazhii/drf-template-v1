from django.contrib import admin
from .models import Community, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.
User = get_user_model()


class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ('phone_number', 'telegram_id',
              'card_number', 'is_suspend', 'comments')


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'date_start',
#                     'date_end', 'tickets', 'price', 'hotel_id')


admin.site.unregister(User)


class UserAdminCustom(UserAdmin):
    # change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Личная информация',
         {'fields': ('first_name', 'last_name',)}),
        ('Разрешения', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')},),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'email', )

    list_display_links = ('email', 'id')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'id', 'email')
    ordering = ('-id',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login',)

    inlines = (ProfileInline,)


admin.site.register(User, UserAdminCustom)
