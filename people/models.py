import settings
import datetime
import dateutil
from django.db import models
from django.utils.translation import ugettext_lazy as _

class PersonType(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    class Meta:
        verbose_name = _('person type')
        verbose_name_plural = _('person types')
        ordering = ('title',)
        abstract = getattr(settings, 'PERSONTYPE_ABSTRACT', True)

    def __unicode__(self):
        return '%s' % self.title

class Person(models.Model):
    """
    A generic model representing an individual

    """
    first_name = models.CharField(_('first name'), blank=True, max_length=100)
    last_name = models.CharField(_('last name'), blank=True, max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    user = models.ForeignKey(User, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(_('gender'), choices=GENDER_CHOIES, blank=True)
    person_type = models.ManyToManyField(PersonType, blank=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')
        ordering = ('last_name', 'first_name')
        abstract = getattr(settings, 'PERSON_ABSTRACT', True)

    def __unicode__(self):
        return '%s' % self.full_name

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @propery
    def age(self):
        TODAY = datetime.date.today()
        return u'%s' % dateutil.relativedelta(TODAY, self.birth_date).years
