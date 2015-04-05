from django.contrib.admin.utils import model_format_dict
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.contenttypes.models import ContentType
from django.db import models
from base.mixins import TimeStampMixin


class EmployerManager(UserManager):

    def __init__(self, *args, **kwargs):
        super(EmployerManager, self).__init__(*args, **kwargs)


class Schedule(models.Model):
    employer = models.OneToOneField('Employer', related_name='schedule')

    def __unicode__(self):
        return str(self.employer)


class Employer(AbstractUser):

    objects = EmployerManager()


    def save(self, *args, **kwargs):
        super(Employer, self).save(*args, **kwargs)

        if not hasattr(self, 'schedule'):
            Schedule.objects.create(employer=self)

    @staticmethod
    def get_by_user(user):
        return Employer.objects.filter(pk=user.pk)

class Department(models.Model):
    title = models.CharField(max_length=255)


class Position(models.Model):
    department = models.ForeignKey(Department)
    employer = models.ForeignKey(Employer)

    hired_at = models.DateField(auto_now_add=True, editable=False)
    fired_at = models.DateField(null=True, blank=True)

    fired = models.BooleanField(default=False)


class Salary(models.Model):
    employer = models.ForeignKey(Employer)
    position = models.ForeignKey(Position)

    amount = models.FloatField()

    payday = models.DateField(auto_now_add=True)


class Warehouse(TimeStampMixin, models.Model):
    pass


class Goods(TimeStampMixin, models.Model):
    cost = models.IntegerField()


class GoodsAtWarehouse(models.Model):
    goods = models.ForeignKey(Goods)
    warehouse = models.ForeignKey(Warehouse)
    count = models.IntegerField()




class Event(TimeStampMixin, models.Model):
    MEETING = 0
    TASK = 1

    EVENT_TYPES = (
        (MEETING, 'Meeting'),
        (TASK, 'Task'),
    )

    schedule = models.ForeignKey(Schedule, related_name='events')
    on_date = models.DateTimeField()

    type = models.IntegerField(choices=EVENT_TYPES)

    title = models.CharField(max_length=255)
    body = models.TextField()




class AbstractActivity(models.Model):
    employer = models.ForeignKey(Employer, related_name="%(class)s_activity")

    class Meta:
        abstract = True


class Email(TimeStampMixin, AbstractActivity):
    body = models.TextField()


class Call(TimeStampMixin, AbstractActivity):
    phone_number = models.CharField(max_length=20)
