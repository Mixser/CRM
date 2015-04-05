from django.contrib.auth.decorators import login_required
from django.db import models

from django.utils.timezone import now


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, default=now)
    changed_at = models.DateTimeField(auto_now=True, default=now)

    def __init__(self, *args, **kwargs):
        super(TimeStampMixin, self).__init__(*args, **kwargs)

    class Meta:
        abstract = True


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)
