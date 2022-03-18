from google.cloud import ndb
from django.urls import reverse
from datazentrik.tests.base import DatastoreTestCase
from datazentrik.models import Redirect

class RedirectTest(DatastoreTestCase):
    """test handling of redirects"""

    def test_not_found(self):
        url = reverse('datazentrik:redirect',kwargs={'slug':'notfound'})
        res = self.client.get(url, follow=False)

        self.assertEqual(res.status_code,404)

    def test_success(self):
        with self.ds_client.context():
            redirect= Redirect(
                key=ndb.Key(Redirect, 'example'),
                destination_url = 'https://example.com/example.txt',
            )
            redirect.put()
        url = reverse('datazentrik:redirect',kwargs={'slug':redirect.key.id()})
        res = self.client.get(url,follow=False)

        self.assertRedirects(
            res,
            redirect.destination_url,
            fetch_redirect_response=False,
            status_code=301,
        )

            