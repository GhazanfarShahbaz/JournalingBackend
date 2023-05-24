from tortoise.fields import IntField, CharField, ForeignKeyField, ManyToManyField
from tortoise.models import Model

class Location(Model):
    id = IntField(pk=True)
    name = CharField(max_length=255)
    url = CharField(null=True)
    entries = ManyToManyField('models.JournalEntry', related_name='locations')
    revisions = ManyToManyField('models.Revision', related_name='locations')
    events = ManyToManyField('models.Event', related_name='locations')