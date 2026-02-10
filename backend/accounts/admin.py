# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Extend/create forms so admin will include extra fields
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "phone_number", "user_profileimage")

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ("username", "email", "phone_number", "user_profileimage")

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "is_superuser")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone_number", "user_profileimage")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "phone_number", "user_profileimage", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("username", "email", "phone_number")
    ordering = ("username",)

admin.site.register(CustomUser, CustomUserAdmin)
