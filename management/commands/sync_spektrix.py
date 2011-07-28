from datetime import datetime

from django.core.management.base import BaseCommand
from django.db.models import get_model
from django.template.defaultfilters import pluralize
from django.contrib.contenttypes.models import ContentType

from spektrix import API
from spektrix.models import Attribute
from spektrix.settings import SPEKTRIX_EVENT_MODEL, SPEKTRIX_TIME_MODEL


def save_attributes(model, lxml_object):
    for attribute in lxml_object.Attributes.getchildren():
        Name = attribute.Name.pyval
        Value = attribute.Value.pyval
        
        # get_or_create is problematic for generic relations
        #   so we'll test if attribute exists first
        kwargs = {
            "content_type": ContentType.objects.get_for_model(model),
            "object_id": model.pk,
            "Name": Name}

        attribute, created = Attribute.objects.\
        get_or_create(**dict(defaults={"Value": Value}, **kwargs))
        if not created:
            for attr, value in kwargs.items():
                setattr(attribute, attr, value)
            attribute.save()


class Command(BaseCommand):

    spektrix = API()
    event_model = get_model(*SPEKTRIX_EVENT_MODEL.split("."))
    time_model = get_model(*SPEKTRIX_TIME_MODEL.split("."))

    new_events = 0
    events_edited = 0

    def handle(self, **options):

        event_list = self.spektrix\
            .GetAllInstancesFromAllAttributes(datetime(2011,1,1))

        # Get / create event
        for lxml_event in event_list.getchildren():
            # Hit spektrix again, as they don't actually supply all the Event attributes
            #    in the GetNextAllAttributes
            full_lxml_event = self.spektrix.GetEventAllAttributes(lxml_event.Id)

            for key in [u'Attributes']:
                if key in full_lxml_event:
                    del(full_lxml_event[key])
            event, created, updated = self.event_model\
                .spektrix.update_or_create(full_lxml_event)

            if created:
                self.new_events +=1
                
            if updated:
                self.events_edited +=1

            # Get / Create attributes
            save_attributes(event, full_lxml_event)
            # get / create event times for event
            for lxml_time in full_lxml_event.Times.getchildren():
                time, created, updated = self.time_model\
                    .spektrix.update_or_create(lxml_time, event=event)

                # Get / Create attributes
                save_attributes(time, lxml_time)

        print "%i Event%s updated" % (self.events_edited, pluralize(self.events_edited))
        print "%i Event%s created" % (self.new_events, pluralize(self.new_events))
