from django.db import models

from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to="blog/images", blank=True)
    author = models.CharField(max_length=100, default="zoro")

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
