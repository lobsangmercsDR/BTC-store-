# Generated by Django 4.2 on 2023-07-06 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0074_transacts_company_transacts_noseguimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 1, 18, 24, 575937, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='y2GOtNfD18E7U6G', max_length=15),
        ),
    ]