"""
This module contains the definition of the `Location` model.

The `Location` model represents a location where an event or journal entry occurred. It has several fields that store information about the location, including its name and URL. It also has several many-to-many relationships with other models, including `Event`, `JournalEntry`, and `Revision`.
"""

from tortoise.fields import IntField, CharField, TextField, ManyToManyField
from tortoise.models import Model

class Location(Model):
    id = IntField(pk=True)
    name = CharField(max_length=255)
    url = TextField(blank=True, null=True)
    entries = ManyToManyField('models.JournalEntry', related_name='location_entries')
    revisions = ManyToManyField('models.Revision', related_name='location_revisions')
    events = ManyToManyField('models.Event', related_name='location_events')