from django.db import models

# Create your models here.
from django.db import models

from loanprofile.storage_backends import PublicMediaStorage, PrivateMediaStorage
# Create your models here.




class profilemodel(models.Model):

    uploaded_at = models.DateTimeField(auto_now_add=True)
    profilepic = models.ImageField(storage=PublicMediaStorage())
    pancard = models.FileField(storage=PublicMediaStorage())
    adhaarcard = models.FileField(storage=PublicMediaStorage())
    anualincome = models.TextField(max_length=100)
    bankdetails = models.TextField(max_length=100)
    def delete(self, *args, **kwargs):
        self.filedata.delete()
        super().delete(*args, **kwargs)