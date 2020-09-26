from django.db import models

class Contact(models.Model):
    contact_name=models.CharField(max_length=50)
    contact_email=models.EmailField(max_length=255)
    message=models.TextField()
    contacted_on=models.DateTimeField(null=True,blank=True,auto_now_add=True)