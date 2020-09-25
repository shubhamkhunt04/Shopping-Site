from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Contact
from .forms import RegisterForm, ContactForm
from django.contrib import admin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=RegisterForm
    ordering = ('email',)
    list_display = ('email','is_active','last_login','is_staff')
    list_filter = ('is_active','is_staff','last_login')
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
    )

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    ordering=('-contacted_on',)
    list_display = ('contact_email','contact_name','message')
    list_filter = ('contacted_on',)
    search_fields = ('contact_name','contact_mail','message')

admin.site.register(Contact,ContactAdmin)
admin.site.register(CustomUser,CustomUserAdmin)