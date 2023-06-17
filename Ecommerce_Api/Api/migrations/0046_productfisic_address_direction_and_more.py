# Generated by Django 4.1.7 on 2023-06-17 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0045_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfisic',
            name='address_direction',
            field=models.CharField(default='C: Martinez Piantini segunda #23', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 19, 35, 33, 306358, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='SyzRoIM0oJy27V1', max_length=15),
        ),
    ]
