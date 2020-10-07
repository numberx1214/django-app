from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title



class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    # todo: create other things like blog page and linking and add moreeee things in data bases
