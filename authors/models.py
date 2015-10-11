from django.db import models
from django.contrib.auth.models import User
from programme.models import Theme
from django.utils import timezone
from time import time
from sorl.thumbnail import get_thumbnail, ImageField
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.doc', '.docx']
    filesize = value.file.size
    if filesize > 5*1024*1024:
        raise ValidationError(u'Max file size 5MB.')
    if not ext in valid_extensions:
        raise ValidationError(u'File type is not supported. Files must be .doc or .docx')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=128, blank = True)
    picture = ImageField(upload_to='user_images', blank=True, null=True)
    url = models.URLField(blank=True, help_text="http://mygroupwebsite.com")
    linkedin = models.URLField(blank=True)
    twitter = models.CharField(max_length=20, blank=True, help_text='e.g. "@pvsat-12"')
    bio = models.TextField(max_length=2000, blank=True)

    def __unicode__(self):
        return self.user.username

class Abstract(models.Model):
    


    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=1000)
    abstract = models.TextField(max_length=50000, null = True, blank=True)
    upload = models.FileField(upload_to='abstract_uploads', validators=[validate_file_extension])
    authors = models.CharField(max_length=500,  help_text='e.g. J. Bloggs, M. C. Hammer ...')
    theme = models.ManyToManyField(Theme)
    unique_id = models.CharField(max_length=11,null=True, blank=True, unique=True)
    
    DELIVERY_CHOICE = (('Oral', 'Oral'), ('Poster', 'Poster'))
    delivery = models.CharField(max_length=6, choices=DELIVERY_CHOICE, default='Oral')

    STATUS = (('Awaiting Decision', 'Awaiting decision'), ('Accepted', 'Accept'), ('Rejected', 'Reject') )
    status = models.CharField(max_length=25, choices=STATUS, default='Awaiting Decision')

    date = models.DateTimeField(default=timezone.datetime.today())
    tags = models.CharField(max_length=250, help_text = "e.g. CdTe, modeling, liverpool")
    author_registered = models.BooleanField(default=False)


    def __unicode__(self):
        return self.title
    


