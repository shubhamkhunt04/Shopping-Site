from django.contrib import admin
from .forms import ContactForm
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    model=Contact
    ordering=('-contacted_on',)
    list_display = ('contact_email','contact_name','message')
    list_filter = ('contacted_on',)
    search_fields = ('contact_name','contact_mail','message')

admin.site.register(Contact,ContactAdmin)