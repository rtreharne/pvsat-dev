from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    logo = models.ImageField(upload_to='logo_images', blank=True)
    OPTIONS = (
        ('99', '-'),
        ('Main', 'Main'),
        ('Associate', 'Associate'),
        ('Poster', 'Poster'),
    )
    type = models.CharField(max_length=129, choices=OPTIONS, default=99, blank=False, null=False)

    def __unicode__(self):
        return self.name


