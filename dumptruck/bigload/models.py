from django.db import models


class Trash(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    contents = models.TextField()

    class Meta:
        ordering = ['created']
