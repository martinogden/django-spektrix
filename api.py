import urllib2
from lxml import objectify

from django.conf import settings
from django.core.cache import cache


class API:

    def __init__(self):
        self.rest_service_url = "https://system.spektrix.com/%s"\
            "/api/v1/eventsrestful.svc" % settings.SPEKTRIX_CLIENT

    def GetAllInstancesFrom(self, date):
        """
        Returns a set of events that have instances that start between
        the given dates, inclusive. This differs from GetFrom in that
        it returns all the instances associated with each event,
        rather than just those that meet the date requirement. Custom
        attributes are included in the returned data for events but
        not for instances.

        @param datetime date
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """
        spektrix_date = self._format_date(date)

        return self._call_spektrix("/alltimes/from?date=%s" % spektrix_date)

    def GetAllInstancesFromAllAttributes(self, date):
        """
        Returns a set of events that have instances that start between
        the given dates, inclusive. This differs from GetFrom in that
        it returns all the instances associated with each event, rather
        than just those that meet the date requirement. Custom attributes
        are included in the returned data for both events and instances.

        @param datetime date
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """

        spektrix_date = self._format_date(date)

        return self._call_spektrix("/alltimes/allattributes/from?"\
            "date=%s" % spektrix_date)

    def GetAllInstancesFromTo(self, dateFrom, dateTo):
        """
        Returns a set of events that have instances that start between
        the given dates, inclusive. This differs from GetFrom in that
        it returns all the instances associated with each event, rather
        than just those that meet the date requirement. Custom attributes
        are included in the returned data for events but not for instances.

        @param datetime dateFrom
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        @param datetime dateTo
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """
        spektrix_from_date = self._format_date(dateFrom)
        spektrix_to_date = self._format_date(dateTo)

        return self._call_spektrix("/alltimes/between?"\
            "dateFrom=%s&dateTo=%s" % (spektrix_from_date, spektrix_to_date))

    def GetAllInstancesFromToAllAttributes(self, dateFrom, dateTo):
        """
        Returns a set of events that have instances that start between
        the given dates, inclusive. This differs from GetFrom in that
        it returns all the instances associated with each event, rather
        than just those that meet the date requirement. Custom attributes
        are included in the returned data for both events and instances.

        @param datetime dateFrom
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        @param datetime dateTo
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """

        spektrix_from_date = self._format_date(dateFrom)
        spektrix_to_date = self._format_date(dateTo)

        return self._call_spektrix("/alltimes/allattributes/between?"\
            "dateFrom=%s&dateTo=%s" % (spektrix_from_date, spektrix_to_date))

    def GetEvent(self, eventId):
        """
        Returns the details of a specific event, including all it's
        instances, attributes and wiki-text (rendered as HTML).
        Custom attributes are included in the returned data for
        events but not for instances.

        @param int eventId
            Integer value specifying the identifier of the Event.
        """

        return self._call_spektrix("/details/%s" % eventId)

    def GetEventAllAttributes(self, eventId):
        """
        Returns the details of a specific event, including all it's
        instances, attributes and wiki-text (rendered as HTML).
        Custom attributes are included in the returned data for
        both events and instances.
        """

        return self._call_spektrix("/details/allattributes/%s" % eventId)

    def GetFrom(self, date):
        """
        Returns a set of events that have instances that start between
        the given dates, inclusive. This differs from GetAllInstancesFrom
        in that the instances associated with each event are filtered
        by the date parameter. Custom attributes are included in the
        returned data for events but not for instances.

        @param datetime date
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """

        spektrix_date = self._format_date(date)
        return self._call_spektrix("/from?date=%s" % spektrix_date)

    def GetFromAllAttributes(self, date):
        """
        Returns a set of events that have instances that start between the
        given dates, inclusive. This differs from GetAllInstancesFrom in
        that the instances associated with each event are filtered by the
        date parameter. Custom attributes are included in the returned
        data for both events and instances.

        @param datetime date
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """

        spektrix_date = self._format_date(date)

        return self._call_spektrix("/allattributes/from?date=%s" % spektrix_date)

    def GetFromTo(self, dateFrom, dateTo):
        """
        Returns a set of events that have instances that start between the
        given dates, inclusive. This differs from GetAllInstancesFrom in
        that the instances associated with each event are filtered by the
        date parameters. Custom attributes are included in the returned
        data for events but not for instances.

        @param datetime dateFrom
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        @param datetime dateTo
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """

        spektrix_from_date = self._format_date(dateFrom)
        spektrix_to_date = self._format_date(dateTo)

        return self._call_spektrix("/between?dateFrom=%s&dateTo=%s"\
            % (spektrix_from_date, spektrix_to_date))

    def GetFromToAllAttributes(self, dateFrom, dateTo):
        """
        Returns a set of events that have instances that start between the
        given dates, inclusive. This differs from GetAllInstancesFrom in that
        the instances associated with each event are filtered by the date
        parameters. Custom attributes are included in the returned data
        for both events and instances.

        @param datetime dateFrom
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        @param datetime dateTo
            Date and time value. Formatted as YYYY-MM-DDTHH:mm:ss
        """

        spektrix_from_date = self._format_date(dateFrom)
        spektrix_to_date = self._format_date(dateTo)

        return self._call_spektrix("/allattributes/between?dateFrom=%s&dateTo=%s"\
            % (spektrix_from_date, spektrix_to_date))

    def GetNext(self, n=1000000):
        """
        Returns a list of the next n events to occur. Custom attributes are
        included in the returned data for events but not for instances.

        @param int n
            Integer specifying the number of events to retrieve
            Set high as a default to *hopefully* pull back all events
        """

        return self._call_spektrix("/next?n=%s" % n)

    def GetNextAllAttributes(self, n=1000000):
        """
        Returns a list of the next n events to occur. Custom attributes are
        included in the returned data for both events and instances.

        @param int n
            Integer specifying the number of events to retrieve
            Set high as a default to *hopefully* pull back all events
        """

        return self._call_spektrix("/allattributes/next?n=%s" % n)

    ###
    def _call_spektrix(self, uri):
        """
        Call Spektrix API, cache results when required
        
        @param str uri
            Which uri the method will call
        """
        url = self.rest_service_url+uri # Set the URL endpoint to call

        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError:
            return False
        else:
            xml = response.read()
            return objectify.fromstring(xml)

    def _format_date(self, date):
        """
        Convert a datetime object to a string date formatted as:
            "YYYY-MM-DDTHH:mm:ss"
        """

        date = date.strftime("%Y-%m-%dT%H:%M:%S")
        return date
