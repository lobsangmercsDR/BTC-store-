# Generated by Django 4.1.7 on 2023-06-22 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0059_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkersolic',
            name='name',
            field=models.CharField(default='asasdasd', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 16, 38, 16, 220280, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='8xlhgSLBny3gv9k', max_length=15),
        ),
    ]