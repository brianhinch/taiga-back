# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0009_userstory_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='is_a_deliverable',
            field=models.BooleanField(default=False, null=False, blank=True, verbose_name=_("represents a deliverable object or document")),
            preserve_default=True,
        ),
    ]
