from tortoise.fields import IntField, CharField, TextField, JSONField, ManyToManyField
from tortoise.models import Model

class Image(Model):
    id = IntField(pk=True)
    data = TextField()
    caption = CharField(max_length=255, default='')
    tags = JSONField(default=[])
    journal_entries = ManyToManyField('models.JournalEntry', related_name='image_entries')