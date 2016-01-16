from django.db import models

MEDIA_TYPES = (
    ('image', 'Image'),
    ('video', 'Video'),
)


class Data(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    hd_url = models.URLField(null=True, blank=True)
    copyright = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True, choices=MEDIA_TYPES)
    explanation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
