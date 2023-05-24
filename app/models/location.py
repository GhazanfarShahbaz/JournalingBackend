from tortoise.fields import IntField, CharField, TextField, ManyToManyField
from tortoise.models import Model

class Location(Model):
    id = IntField(pk=True)
    name = CharField(max_length=255)
    url = TextField(blank=True, null=True)
    entries = ManyToManyField('models.JournalEntry', related_name='location_entries')
    revisions = ManyToManyField('models.Revision', related_name='location_revisions')
    events = ManyToManyField('models.Event', related_name='location_events')