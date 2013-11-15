from django.db import models
from jqueryfileupload.models import *


class Video(UploadedFile):
	encoded = models.BooleanField(default=False)
	
