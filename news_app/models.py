from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='media/news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #Category modelga boglandi
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True) #not change
    updated_time = models.DateTimeField(auto_now=True) #can change
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)
    class Meta:
        ordering = ['-published_time']
    def __str__(self):
        return self.title

