"""
This module contains the definition of the `Image` model.

The `Image` model represents an image that can be associated with a journal entry. It has several fields that store information about the image, including its data, caption, and tags. It also has a many-to-many relationship with the `JournalEntry` model.
"""

from tortoise.fields import IntField, CharField, TextField, JSONField, ManyToManyField
from tortoise.models import Model

class Image(Model):
    id = IntField(pk=True)
    data = TextField()
    caption = CharField(max_length=255, default='')
    tags = JSONField(default=[])
    journal_entries = ManyToManyField('models.JournalEntry', related_name='image_entries')