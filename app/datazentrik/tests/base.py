"""
Base test classes
"""
import inspect #inspect and retrieve values in module
from google.cloud import ndb #datastore manager thingy
from django.conf import settings
from django.test import ( #modify and test 
    SimpleTestCase, 
    override_settings,
    Client,
)
from app.datastore import get_client
from datazentrik import models 

TEST_NAMESPACE = f'test_{settings.DATASTORE_NAMESPACE}'

@override_settings(DATASTORE_NAMESPACE=TEST_NAMESPACE)
class DatastoreTestCase(SimpleTestCase):
    """class for datastore tests"""

    def setUp(self):
        self.client = Client()
        self.ds_client = get_client()

    def _clear_entities(self):

        """clear db after tests"""
        classes = inspect.getmembers(models, inspect.isclass)
        model_classes = []
        for name,obj in classes:
            if issubclass(obj,ndb.Model):
                model_classes.append(obj)
        
        client = get_client()
        with client.context():
            for model  in model_classes:
                ndb.delete_multi(model.query().iter(keys_only=True))

        def tearDown(self):
            self._clear_entitites()