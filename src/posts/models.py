from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title           = models.CharField(max_length=150)
    content         = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image           = models.ImageField(upload_to='posts/', blank=True, null=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    
    class Meta:
        verbose_name        = 'Post'
        verbose_name_plural = 'Posts'
        ordering            = ('id',)
