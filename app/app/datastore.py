"""
Google Cloud Datastore helpers.
"""

from google.cloud import ndb
from google.auth.credentials import AnonymousCredentials
from django.test.runner import DiscoverRunner
from django.conf import settings

def get_client():
    if settings.IS_GAE:
        return ndb.Client(namespace=settings.DATASTORE_NAMESPACE)
    return ndb.Client(
        credentials=AnonymousCredentials(),
        project=settings.GOOGLE_CLOUD_PROJECT,
        namespace=settings.DATASTORE_NAMESPACE,
    )


class NDBMiddleware:
    """Middlware for handling NDB context."""

    def __init__(self, get_response):
        """Create client."""
        self.get_response = get_response
        self.client = get_client()

    def __call__(self, request):
        """Create a context."""
        context = self.client.context()
        request.ndb_context = context
        with context:
            response = self.get_response(request)

        return response
class TestRunner(DiscoverRunner):
    """TEST SUITE RUNNER USING DATASTORE"""

    def setup_database(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass