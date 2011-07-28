from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings
from django.template.defaultfilters import slugify

from spektrix.managers import SpektrixManager
from spektrix.settings import SPEKTRIX_EVENT_MODEL, SPEKTRIX_TIME_MODEL


class BaseSpektrixEvent(models.Model):
    """
    Base class with attributes matching spektrix "Event" object schema

    This class must be subclassed
    """

    class Meta:
        abstract = True
        ordering = ["FirstInstance", "LastInstance", "Name"]

    spektrix = SpektrixManager()
    objects = models.Manager()

    Id = models.PositiveIntegerField(primary_key=True)
    WebEventId = models.CharField(max_length=25, blank=True, null=True)

    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    Html = models.TextField("HTML", blank=True, null=True)

    ImageUrl = models.URLField("Image URL", blank=True, null=True)
    ThumbnailUrl = models.URLField("Thumbnail URL", blank=True, null=True)

    FirstInstance = models.DateTimeField("First Instance")
    LastInstance = models.DateTimeField("Last Instance")
    Duration = models.IntegerField()

    Attributes = generic.GenericRelation("spektrix.Attribute")

    OnSaleOnWeb = models.BooleanField("On sale on web")

    def __unicode__(self):
        return self.Name


class BaseSpektrixTime(models.Model):
    """
    Base class with attributes matching spektrix "EventTime" object schema

    This class must be subclassed
    """

    class Meta:
        abstract = True
        ordering = ["Time"]

    spektrix = SpektrixManager()
    objects = models.Manager()

    event = models.ForeignKey(SPEKTRIX_EVENT_MODEL, related_name="Times")

    EventInstanceId = models.PositiveIntegerField(primary_key=True)
    WebInstanceId = models.CharField(max_length=25, blank=True, null=True)

    SeatsLocked = models.IntegerField()
    Capacity = models.IntegerField()
    SeatsSelected = models.IntegerField()
    SeatsSold = models.IntegerField()
    SeatsAvailable = models.IntegerField()
    SeatsReserved = models.IntegerField()

    Time = models.DateTimeField()

    Attributes = generic.GenericRelation("spektrix.Attribute")

    OnSaleOnWeb = models.BooleanField()


class Attribute(models.Model):
    """
    Key: value pairs. Uses django generic relationships
        to associate with any object

    N.B. This model does NOT need to be subclassed
    """
    Name = models.CharField(max_length=255)
    Value = models.TextField(max_length=255)

    # Polymorphic / generic relationship bits
    tag = models.SlugField(max_length=255)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    def __unicode__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.tag = slugify(self.Value)
        return super(Attribute, self).save(*args, **kwargs)


"""
If Event and Time models have not been defined in settings,
    we can use these defaults
"""
if not hasattr(settings, "SPEKTRIX_EVENT_MODEL"):

    class Event(BaseSpektrixEvent):
        pass

if not hasattr(settings, "SPEKTRIX_TIME_MODEL"):

    class Time(BaseSpektrixTime):
        pass
