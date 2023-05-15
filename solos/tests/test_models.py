from django.test import TestCase
from jmad.solos.models import Solo
class SoloModelTestCase(TestCase):
    def setUp(self):
        self.solo = Solo.objects.create(track = 'falling in Love with Love', artist = 'Oscar Peterson',instrument = 'piano')
    def test_solo_basic(self):
        """Test the basic functionality of Solo"""
        self.assertEqual(self.solo.artist,'Peterson')