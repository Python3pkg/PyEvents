from unittest import TestCase

from pyevents.manager import EventDispatcher
from pyevents.event import Event


class TestDispatcher(TestCase):

    def setUp(self):
        self.manager = EventDispatcher()
        self.called = False

    def _check_callback(self, evt):
        self.called = True

    def test_can_add_a_listener(self):
        self.manager.add_listener('test', self._check_callback)
        self.assertTrue(self.manager.has_listener('test',
                                                  self._check_callback))

    def test_can_remove_a_listener(self):
        self.manager.add_listener('test', self._check_callback)
        self.manager.remove_listener('test', self._check_callback)
        self.assertFalse(self.manager.has_listener('test',
                                                   self._check_callback))

    def test_can_dispatch_a_to_a_listener(self):
        self.manager.add_listener('Event', self._check_callback)
        self.manager.dispatch(Event('Event', 'awesome'))
        self.assertTrue(self.called)

    def test_can_dispatch_event_not_listening(self):
        self.manager.dispatch(Event('Event', 'awesome'))
        self.assertFalse(self.called)

    def test_can_remove_added_event(self):
        self.manager.add_listener('Event', self._check_callback)
        self.manager.remove_listener('Event', self._check_callback)
        self.manager.dispatch(Event('Event', 'awesome'))
        self.assertFalse(self.called)
