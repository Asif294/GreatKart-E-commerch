from django.db import models

class category(models.Model):
    category=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='photos/categories/',blank=True)


    class Meta:
        verbose_name='category'
        # verbose_plural_name='categories'


    def __str__(self):
        return self.category

