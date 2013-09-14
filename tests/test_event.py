from unittest import TestCase

from pyevents.event import Listener


class TestListener(TestCase):
    def _check_callback(self, evt):
        pass

    def test_we_should_be_able_to_compare_listener_objects(self):
        exemplar = Listener('test', self._check_callback)
        expected = Listener('test', self._check_callback)
        bad_expect = Listener('badtest', self._check_callback)

        self.assertEqual(exemplar, expected)
        self.assertNotEqual(exemplar, bad_expect)
