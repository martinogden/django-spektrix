import time
import lxml
from django.core.mail import send_mail
from django.db import models
from datetime import datetime

from spektrix import API
from spektrix.settings import SPEKTRIX_DATE_TYPES


def normalize_date(date_string):
    """
    Convert Spektrix 'YYYY-MM-DDTHH:mm:ss' string to datetime object
    """
    return datetime(*time.strptime(date_string, "%Y-%m-%dT%H:%M:%S")[:6])


def clean_dict(dirty_dict):
    """
    Convert all xml datatypes to simple Python types before saving to database
    """
    SPEKTRIX_DATE_TYPES = ["FirstInstance", "LastInstance", "Time"]

    clean_dict = {}
    for key in dirty_dict.keys():
        # Only force python object type if lxml will let us
        #   i.e. not if this is a 'collection'
        if hasattr(dirty_dict[key], "pyval"):
            clean_dict[key] = dirty_dict[key].pyval
            if key in SPEKTRIX_DATE_TYPES:
                clean_dict[key] = normalize_date(clean_dict[key])

    return clean_dict


class SpektrixManager(models.Manager):
    """
    Save Event / Time object from Spektrix XML response to our database
    """

    def update_or_create(self, *args, **kwargs):
        """
        @param object
            lxml "objectify" type object
        """

        # Get the object attributes as a dict
        attrs = args[0].__dict__
        attrs = clean_dict(attrs)

        # get object pk name for get_or_create below
        if 'Id' in attrs:
            ID = attrs.pop('Id')
        elif 'EventInstanceId' in attrs:
            ID = attrs.pop('EventInstanceId')
        else:
            ID = None
        for key in ['Attributes']:
            if key in attrs:
                del(attrs[key])

        obj, created = self.get_query_set().get_or_create(pk=ID, defaults=dict(attrs, **kwargs))
        if created:
            return obj, True, False
        else:
            for attr, value in dict(attrs, **kwargs).items():
                setattr(obj, attr, value)

            obj.save()

            return obj, False, True
