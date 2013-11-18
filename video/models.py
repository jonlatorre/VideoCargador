# encoding: utf-8
from django.db import models
import os
from mencoder import *


class Video(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    file = models.FileField(upload_to="uploaded_videos")
    slug = models.SlugField(max_length=50, blank=True)
    mp4_encoded = models.BooleanField(default=False)
    mp4_file = models.FileField(upload_to="converted_videos", blank=True)
    mp4_url = models.BooleanField(default=False)
    flv_encoded = models.BooleanField(default=False)
    flv_file = models.FileField(upload_to="converted_videos", blank=True)
    flv_url = models.BooleanField(default=False)

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
    def encode_mp4(self):
        print "Vamos a convertir a mp4"
        destino = self.mp4_file.storage.base_location
        destino = os.path.join(destino,"converted_videos")
        ret,salida = call_mencoder_mp4(self.file.path,destino)
        if ret == 0:
            print "Codificacion OK"
            self.mp4_file.name = "converted_videos/"+salida
            self.mp4_encoded = True
            self.save()
    def upload_mp4(self):
        print "Subimos el MP4"
