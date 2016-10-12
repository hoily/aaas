from django.db import models
from project.common.models import Entity


class Image(Entity):
    published = models.BooleanField(default=True)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    file = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.file.name
