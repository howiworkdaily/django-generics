from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from tagging.models import Tag
from content.models import Entry, ContentItemBase
import settings
from django.db import models

CT = ContentType.objects.get_for_model

class ExampleContentItem(ContentItemBase):
    name = models.CharField(max_length=10)


class EntryTest(TestCase):
    """
    Test entry model.

    """

    fixtures = ["tagging.json", "entry.json",]

    def setUp(self):
	    pass

    def tearDown(self):
        pass

    def test_confirm_type(self):
        """
        Confirm the first object instance in the Entry table is the correct type.

        """   
        obj = Entry.objects.all().get()    
        utype = ContentType.objects.get_for_model(User)

        self.assertEqual(obj.content_type, utype) 


class ContentItemBase(TestCase):
    """
    Test ContentItemBase model.

    """

    def test_is_abc(self):
        #TODO
        pass

    def test_is_mti(self):
        #TODO
        pass

