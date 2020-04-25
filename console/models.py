from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class MachineImages(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    screenshots = models.FileField(upload_to='media/machine-images', null=False, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.title
