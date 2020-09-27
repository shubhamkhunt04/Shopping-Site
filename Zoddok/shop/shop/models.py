from django.db import models
from django.utils.safestring import mark_safe

class Contact(models.Model):
    contact_name=models.CharField(max_length=50)
    contact_email=models.EmailField(max_length=255)
    message=models.TextField()
    contacted_on=models.DateTimeField(null=True,blank=True,auto_now_add=True)

class Team(models.Model):
    Member_Name = models.CharField(blank=False,max_length=70)
    Member_Position = models.CharField(blank=False,max_length=100)
    Member_Profile = models.ImageField(blank=False,upload_to="img/")
    Member_FaceBook_Account = models.CharField(blank=True,max_length=255)
    Member_Twitter_Account = models.CharField(blank=True,max_length=255)
    Member_Instagram_Account = models.CharField(blank=True,max_length=255)
    Member_Linkdin_Account = models.CharField(blank=True,max_length=255)

    def image_tag(self):
        if self.Member_Profile is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.Member_Profile.url))
        else:
            return ""
    
    def __str__(self):
        return self.Member_Name