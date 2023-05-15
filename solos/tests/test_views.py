from django.test import TestCase, RequestFactory
from jmad.solos.views import index
from django.db.models.query import QuerySet


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the correct template
        :return:
        """
        response = self.client.get('/',{'instrument':'drums'})
        self.assertIs(type(response.context['solos']), QuerySet)
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code,200)
