from django.contrib import admin

# Register your models here.

from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin
from .models import User,Hospital,Appointment,Invoice
from .forms import UserChangeForm,UserCreationForm
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(Invoice)

@register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'name',)
    list_filter = ('is_active', 'is_superuser')
    fieldsets = (
        ('User Data', {'fields': ('email', 'name', 'password','mobile','allergies','weight','hospital','invoices','appointments','dob')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),  
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
