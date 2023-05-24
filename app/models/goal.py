from tortoise.fields import IntField, CharField, TextField, JSONField, BooleanField, DateField, FloatField
from tortoise.models import Model

class Goal(Model):
    id = IntField(pk=True)
    goal = CharField(max_length=255)
    comments = TextField(default='')
    category = CharField(max_length=255)
    priority = FloatField()
    start_date = DateField()
    target_date = DateField()
    completed = BooleanField(default=False)
    current_progress_index = IntField(null=True)
    progress_action_items = JSONField(default=list)
    date_achieved = DateField(null=True)
    date_set = DateField()
    motivators = JSONField(default=list)
    reminders = JSONField(default=list)
    supporters = JSONField(default=list)
    target_value = FloatField()
    units = CharField(max_length=255)

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