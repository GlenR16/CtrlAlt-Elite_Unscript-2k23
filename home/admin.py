
from django.contrib import admin

# Register your models here.

from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin
from .models import User,UploadedFile
from .forms import UserChangeForm,UserCreationForm
# Register your models here.

admin.site.register(UploadedFile)

@register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('id','email', 'name',)
    list_filter = ('is_active', 'is_superuser')
    fieldsets = (
        ('User Data', {'fields': ('email', 'name', 'password','files')}),
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



# admin.site.register(Event)
