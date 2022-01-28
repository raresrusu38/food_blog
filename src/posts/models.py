from django.db                      import models
from django.conf                    import settings
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    title           = models.CharField(max_length=150)
    slug            = models.SlugField(editable=False, default='slug')
    
    
    def __str__(self):
        return self.title
    
    def post_count(self):
        return self.posts.all().count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        

    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'
        ordering            = ('id',)
        

class Post(models.Model):
    title           = models.CharField(max_length=150)
    slug            = models.SlugField(default='slug', editable=False)
    content         = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image           = models.ImageField(upload_to='posts/', blank=True, null=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="posts")
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    
    class Meta:
        verbose_name        = 'Post'
        verbose_name_plural = 'Posts'
        ordering            = ('id',)
