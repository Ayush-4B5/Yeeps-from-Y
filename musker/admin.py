from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from .models import Profile, Meep

# Unregister default Group model
admin.site.unregister(Group)


# Inline Profile model with User admin
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend UserAdmin from BaseUserAdmin
class UserAdmin(BaseUserAdmin):
    # Define fieldsets to customize the user creation form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Include ProfileInline inlines
    inlines = [ProfileInline]
    # Customize list_display to display additional fields in the user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    # Override has_delete_permission to allow superusers to delete other superusers
    def has_delete_permission(self, request, obj=None):
        # Allow superusers to delete other superusers
        return request.user.is_superuser


# Reregister User with custom admin configuration
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register Meep model
admin.site.register(Meep)
