from django.core.management.base import BaseCommand, CommandError
from video.models import *

class Command(BaseCommand):
	 def handle(self, *args, **options):
		 v = Video.objects.get(id=1)
		 v.encode_mp4()
		
		
