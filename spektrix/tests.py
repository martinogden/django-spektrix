from django.test import TestCase
from django.core import management
from django.db.models import get_model

from spektrix.settings import SPEKTRIX_EVENT_MODEL, SPEKTRIX_TIME_MODEL
from spektrix import API


class SimpleTest(TestCase):

    def setUp(self):
        self.event_model = get_model(*SPEKTRIX_EVENT_MODEL.split("."))
        self.time_model = get_model(*SPEKTRIX_TIME_MODEL.split("."))
        self.spektrix = API()
        self.spektrix_event_list = self.spektrix.GetNextAllAttributes()\
            .getchildren()

    def testSync(self):
        """
        Test 'sync_spektrix' management command is returning
            correct number Events / Times
        """

        management.call_command("sync_spektrix")

        spektrix_event_count = len(self.spektrix_event_list)

        self.assertEqual(spektrix_event_count,\
            self.event_model.objects.count())

        for spektrix_event in self.spektrix_event_list:
            event = self.event_model.objects.get(pk=spektrix_event.Id.pyval)
            time_count = len(spektrix_event.Times.getchildren())

            self.assertEqual(time_count, event.Times.count())

    def testGetOrCreateEvent(self):
        """
        Test managers.SpektrixManager.get_or_create()
            saves an Event model using XML data from spektrix
        """
        spektrix_event = self.spektrix_event_list[0]
        event, created, updated = self.event_model\
            .spektrix.update_or_create(spektrix_event)

        self.assertTrue(created)
