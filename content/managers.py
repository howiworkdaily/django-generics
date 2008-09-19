from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db.models import Manager
from datetime import datetime

class EntryManager(Manager):
	
    def get_published(self):
        return self.get_query_set().filter(publish_on__lt = datetime.now())
