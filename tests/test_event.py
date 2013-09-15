from unittest import TestCase

from pyevents.event import Event, Listener


class TestListener(TestCase):
    def _check_callback(self, evt):
        pass

    def test_we_should_be_able_to_compare_listener_objects(self):
        exemplar = Listener('test', self._check_callback)
        expected = Listener('test', self._check_callback)
        bad_expect = Listener('badtest', self._check_callback)

        self.assertEqual(exemplar, expected)
        self.assertNotEqual(exemplar, bad_expect)


class TestEvent(TestCase):
    def test_compare_two_instances_with_same_content(self):
        evt1 = Event('test', 'random_str')
        evt2 = Event('test', 'random_str')

        self.assertEqual(evt1, evt2)
