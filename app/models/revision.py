from tortoise.models import Model
from tortoise.fields import IntField, CharField, TextField, DatetimeField, JSONField, ForeignKeyField, ManyToManyField

class Revision(Model):
    id = IntField(pk=True)
    content = TextField()
    author = CharField(max_length=255)
    mood = CharField(max_length=255, null=True)
    weather = CharField(max_length=255, null=True)
    rating = IntField(min_value=1, max_value=10, default=1)
    comments = TextField(default='')
    created_at = DatetimeField(auto_now_add=True)
    tags = JSONField(default=[])
    people = JSONField(default=[])
    entry = ForeignKeyField('models.JournalEntry', related_name='revision_entry')
    image = ForeignKeyField('models.Image', related_name='revision_image', null=True)
    locations = ManyToManyField('models.Location', related_name='revision_locations', null=True)
    events = ManyToManyField('models.Event', related_name='revision_events', null=True)