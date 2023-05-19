from tortoise import Tortoise, fields, run_async
from tortoise.models import Model


class JournalEntry(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    author = fields.CharField(max_length=255)
    mood = fields.CharField(max_length=255, null=True)
    weather = fields.CharField(max_length=255, null=True)
    rating = fields.IntField(min_value=1, max_value=10, default=1)
    comments = fields.TextField(default='')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    tags = fields.JSONField(default=[])
    people = fields.JSONField(default=[])
    goal = fields.ForeignKeyField('models.Goal', related_name='journal_entries', null=True)
    image = fields.ForeignKeyField('models.Image', related_name='journal_entries', null=True)
    locations = fields.ManyToManyField('models.Location', related_name='entries', null=True)
    events = fields.ManyToManyField('models.Event', related_name='entries', null=True)


class Revision(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=255)
    mood = fields.CharField(max_length=255, null=True)
    weather = fields.CharField(max_length=255, null=True)
    rating = fields.IntField(min_value=1, max_value=10, default=1)
    comments = fields.TextField(default='')
    created_at = fields.DatetimeField(auto_now_add=True)
    tags = fields.JSONField(default=[])
    people = fields.JSONField(default=[])
    entry = fields.ForeignKeyField('models.JournalEntry', related_name='revisions')
    image = fields.ForeignKeyField('models.Image', related_name='revisions', null=True)
    locations = fields.ManyToManyField('models.Location', related_name='revisions', null=True)
    events = fields.ManyToManyField('models.Event', related_name='revisions', null=True)

class Image(Model):
    id = fields.IntField(pk=True)
    data = fields.TextField()
    caption = fields.CharField(max_length=255, default='')
    tags = fields.JSONField(default=[])
    journal_entries = fields.ManyToManyField('models.JournalEntry', related_name='images')
    

class Location(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    url = fields.CharField(null=True)
    entries = fields.ManyToManyField('models.JournalEntry', related_name='locations')
    revisions = fields.ManyToManyField('models.Revision', related_name='locations')
    events = fields.ManyToManyField('models.Event', related_name='locations')


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    location = fields.ForeignKeyField('models.Location', related_name='events')
    description = fields.TextField(default='')
    attendees = fields.JSONField(default=list)
    reminder_time = fields.DatetimeField(null=True)
    status = fields.CharField(max_length=255)
    organizer = fields.CharField(max_length=255)
    entries = fields.ManyToManyField('models.JournalEntry', related_name='events')
    revisions = fields.ManyToManyField('models.Revision', related_name='events')
    locations = fields.ManyToManyField('models.Location', related_name='events')


class Goal(Model):
    id = fields.IntField(pk=True)
    goal = fields.CharField(max_length=255)
    comments = fields.TextField(default='')
    category = fields.CharField(max_length=255)
    priority = fields.FloatField()
    start_date = fields.DateField()
    target_date = fields.DateField()
    completed = fields.BooleanField(default=False)
    current_progress_index = fields.IntField(null=True)
    progress_action_items = fields.JSONField(default=list)
    date_achieved = fields.DateField(null=True)
    date_set = fields.DateField()
    motivators = fields.JSONField(default=list)
    reminders = fields.JSONField(default=list)
    supporters = fields.JSONField(default=list)
    target_value = fields.FloatField()
    units = fields.CharField(max_length=255)

    async def save(self, *args, **kwargs):
        if self.current_progress_index is not None:
            if self.current_progress_index < 0 or self.current_progress_index >= len(self.progress_action_items):
                raise ValueError(f"Invalid current progress index {self.current_progress_index}")
        await super().save(*args, **kwargs)

    @property
    def current_progress(self):
        if self.current_progress_index is not None:
            return self.progress_action_items[self.current_progress_index]
        else:
            return None


Tortoise.init_models(['app.models'], 'models')