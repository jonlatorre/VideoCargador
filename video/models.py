# encoding: utf-8
from django.db import models


class Video(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    file = models.FileField(upload_to="videos")
    slug = models.SlugField(max_length=50, blank=True)
    mp4_encoded = models.BooleanField(default=False)
    #mp4_url = models.BooleanField(default=False)
    flv_encoded = models.BooleanField(default=False)
    #flv_url = models.BooleanField(default=False)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('video-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Video, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Video, self).delete(*args, **kwargs)
