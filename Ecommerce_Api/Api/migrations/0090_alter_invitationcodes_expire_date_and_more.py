# Generated by Django 4.2.4 on 2023-08-04 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0089_remove_productdigit_actquantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 18, 15, 26, 305471, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='ZrYA5P62Qtnb8gr', max_length=15),
        ),
    ]
