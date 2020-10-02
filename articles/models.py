from django.db import models
from django.utils import timezone

class Category(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    status = models.BooleanField(default=True , verbose_name="show this ?")
    position = models.IntegerField(verbose_name="position")

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

#nepton,nepton,nepton,...

class articles(models.Model):
    STATUS_CHOICES=(
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    Category = models.ManyToManyField(Category, verbose_name="Category")
    #body=models.TextField()
    #date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
