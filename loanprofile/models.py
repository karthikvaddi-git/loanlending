from django.db import models

# Create your models here.
from django.db import models

from loanprofile.storage_backends import PublicMediaStorage, PrivateMediaStorage
# Create your models here.


class upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filedata = models.FileField(storage=PublicMediaStorage())

    def delete(self, *args, **kwargs):
        self.filedata.delete()
        super().delete(*args, **kwargs)


class uploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    profilepic=models.ImageField(storage=PrivateMediaStorage())
    pancard = models.FileField(storage=PrivateMediaStorage())
    adhaarcard=models.FileField(storage=PrivateMediaStorage())
    anualincome=models.TextField(max_length=100)
    bankdetails=models.TextField(max_length=100)



    def delete(self, *args, **kwargs):
        self.filedata.delete()
        super().delete(*args, **kwargs)