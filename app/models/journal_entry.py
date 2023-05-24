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
    goal = ForeignKeyField('models.Goal', related_name='journal_entries', null=True)
    image = ForeignKeyField('models.Image', related_name='journal_entries', null=True)
    locations = ManyToManyField('models.Location', related_name='entries', null=True)
    events = ManyToManyField('models.Event', related_name='entries', null=True)
