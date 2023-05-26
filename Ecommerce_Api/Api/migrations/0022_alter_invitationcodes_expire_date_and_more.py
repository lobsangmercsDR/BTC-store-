# Generated by Django 4.1.7 on 2023-05-23 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0021_invitationcodes_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 13, 5, 39, 398712, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='LPeSE642UB1oVzc', max_length=15, unique=True),
        ),
    ]