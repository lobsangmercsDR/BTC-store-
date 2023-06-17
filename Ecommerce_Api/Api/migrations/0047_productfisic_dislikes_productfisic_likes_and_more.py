# Generated by Django 4.1.7 on 2023-06-17 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0046_productfisic_address_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfisic',
            name='dislikes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='productfisic',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 20, 31, 38, 411766, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='hCBL4wULxVHFdEi', max_length=15),
        ),
    ]
