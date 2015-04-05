from django.db import models

from django.utils.timezone import now


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, default=now)
    changed_at = models.DateTimeField(auto_now=True, default=now)

    def __init__(self, *args, **kwargs):
        super(TimeStampMixin, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True
