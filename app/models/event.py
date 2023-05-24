from tortoise.fields import IntField, CharField, TextField, JSONField, DatetimeField, ForeignKeyField, ManyToManyField
from tortoise.models import Model

class Event(Model):
    id = IntField(pk=True)
    name = CharField(max_length=255)
    start_time = DatetimeField()
    end_time = DatetimeField()
    description = TextField(default='')
    attendees = JSONField(default=list)
    reminder_time = DatetimeField(null=True)
    status = CharField(max_length=255)
    organizer = CharField(max_length=255)
    entries = ManyToManyField('models.JournalEntry', related_name='events_entries')
    revisions = ManyToManyField('models.Revision', related_name='events_revisions')
    locations = ManyToManyField('models.Location', related_name='events_locations')