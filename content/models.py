from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
import enums, managers
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import settings


class ContentItemBase(models.Model):
    """
    Defines fields you find on most content items.

    """

    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'),)
    tags = TagField()
    status = models.IntegerField(_('status'), choices=enums.CONTENT_STATUS_CHOICES, default=enums.DEFAULT_CONTENT_STATUS)
    comment_status = models.IntegerField(_('comment status'), choices=enums.COMMENT_STATUS_CHOICES, default=enums.DEFAULT_COMMENT_STATUS)
    created_on = models.DateTimeField(_('created on'), editable=False, )
    updated_on = models.DateTimeField(_('updated on'), editable=False)
    publish_on = models.DateTimeField(_('publish on'), )

    class Meta:
        abstract = getattr(settings, 'CONTENTITEMBASE_ABSTRACT', True)

    
    def pre_save(self):
        if self.id is None:
            self.created_on = datetime.now()  
        self.updated_on = datetime.now()

    def __unicode__(self):
        return self.title        



class Entry(models.Model):
    """
    A generic entry model denormalized for performance and useful for providing aggregation among various content types.

    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = generic.GenericForeignKey()
    publish_on = models.DateTimeField()
    tags = TagField()

    objects = managers.EntryManager()
   
    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        ordering = ('-publish_on',)

    def get_absolute_url(self):
        return self.object.get_absolute_url()

    def __unicode__(self):
        try:
            return self.object.__unicode__()
        except:
            if hasattr(self.object.title):
                return self.object.title
            else:
                return self.object.__class__
