from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.core.validators import FileExtensionValidator
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='media/post-images', default='media/post-images/default.jpg', validators=[
                             FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
