from django.db import models

# allows database to hold uploaded file until it is analyzed
class Files(models.Model):
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.upload.name
   