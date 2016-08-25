from django.db import models, migrations
from django_hstore import hstore

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS hstore")
    ]

class FormBuilder(models.Model):
    data = hstore.DictionaryField()  # can pass attributes like null, blank, etc.
    builder = hstore.DictionaryField()  # can pass attributes like null, blank, etc.

    objects = hstore.HStoreManager()
