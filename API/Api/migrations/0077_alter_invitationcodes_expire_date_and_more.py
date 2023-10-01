# Generated by Django 4.1.7 on 2023-07-06 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0076_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 15, 23, 26, 528998, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='G0z7ydNelk9xPGb', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='userBalance',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='withdrawals',
            name='fecha_review',
            field=models.DateField(default=None),
        ),
    ]