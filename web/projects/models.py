from django.db import models
from markdownx.fields import MarkdownxFormField
import datetime


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    tagline = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=datetime.date.today)

    stack = models.TextField()
    description = models.TextField()
    additional_notes = models.TextField()
    wish_list = models.TextField()

    demo_url = models.URLField()
    github_url = models.URLField()
    thumbnail_image_url = models.URLField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title
