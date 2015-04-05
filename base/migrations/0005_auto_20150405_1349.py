# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forward(apps, schema):
    Employer = apps.get_model('base', 'Employer')
    Schedule = apps.get_model('base', 'Schedule')

    for emp in Employer.objects.all():
        if not hasattr(emp, 'schedule'):
            Schedule.objects.create(employer=emp)

def backward(apps, schema):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20150405_1349'),
    ]

    operations = [
        migrations.RunPython(forward, reverse_code=backward)
    ]
