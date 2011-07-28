from django.conf import settings

# These are fields in the spektrix xml response
#   which should be converted to a datetime object
DEFAULT_SPEKTRIX_DATE_TYPES = ["FirstInstance", "LastInstance", "Time"]
SPEKTRIX_DATE_TYPES = getattr(settings,\
    "SPEKTRIX_DATE_TYPES", DEFAULT_SPEKTRIX_DATE_TYPES)

# This should be overidden in global settings to specify an 
#    Event model which subclasses spektrix.SpektrixEvent
SPEKTRIX_EVENT_MODEL = getattr(settings,\
    "SPEKTRIX_EVENT_MODEL", "spektrix.Event")

# Same as above, but for the spektrix.SpektrixTime model
SPEKTRIX_TIME_MODEL = getattr(settings,\
    "SPEKTRIX_TIME_MODEL", "spektrix.Time")
