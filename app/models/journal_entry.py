"""
This module contains the definition of the `JournalEntry` model.

The `JournalEntry` model represents a journal entry written by a user. It has several fields that store information about the entry, including its title, content, author, mood, and weather. It also has several many-to-many relationships with other models, including `Goal`, `Location`, `Image`, and `Event`.
"""

from tortoise.models import Model
from tortoise.fields import IntField , CharField, TextField, DatetimeField, DateField, JSONField, ForeignKeyField, ManyToManyField

class JournalEntry(Model):
    id = IntField(pk=True)
    title = CharField(max_length=255)
    content = TextField()
    author = CharField(max_length=255)
    mood = CharField(max_length=255, null=True)
    weather = CharField(max_length=255, null=True)
    rating = IntField(min_value=1, max_value=10, default=1)
    comments = TextField(default='')
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)
    tags = JSONField(default=[])
    people = JSONField(default=[])
    goal = ManyToManyField('models.Goal', related_name='journal_goal', null=True)
    image = ForeignKeyField('models.Image', related_name='journal_image', null=True)
    locations = ManyToManyField('models.Location', related_name='journal_locations', null=True)
    events = ManyToManyField('models.Event', related_name='journal_events', null=True)
