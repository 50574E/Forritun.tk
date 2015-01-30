from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=False)
    date_modified = models.DateTimeField('date modified', auto_now=True)
    slug = models.SlugField()
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProgrammingLanguage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Resource(models.Model):
    language = models.ForeignKey(ProgrammingLanguage)
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField('date created', auto_now_add=True, editable=False)
    date_modified = models.DateTimeField('date modified', auto_now=True)
    slug = models.SlugField()
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Resource, self).save(*args, **kwargs)

    def __str__(self):
        return self.link