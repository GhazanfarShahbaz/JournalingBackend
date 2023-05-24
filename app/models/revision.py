from tortoise.models import Model
from tortoise.fields import IntField, CharField, TextField, DateTimeField, JSONField, ForeignKeyField, ManyToManyField

class Revision(Model):
    id = IntField(pk=True)
    content = TextField()
    author = CharField(max_length=255)
    mood = CharField(max_length=255, null=True)
    weather = CharField(max_length=255, null=True)
    rating = IntField(min_value=1, max_value=10, default=1)
    comments = TextField(default='')
    created_at = DateTimeField(auto_now_add=True)
    tags = JSONField(default=[])
    people = JSONField(default=[])
    entry = ForeignKeyField('models.JournalEntry', related_name='revisions')
    image = ForeignKeyField('models.Image', related_name='revisions', null=True)
    locations = ManyToManyField('models.Location', related_name='revisions', null=True)
    events = ManyToManyField('models.Event', related_name='revisions', null=True)