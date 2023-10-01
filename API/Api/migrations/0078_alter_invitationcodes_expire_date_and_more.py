# Generated by Django 4.1.7 on 2023-07-06 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0077_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 15, 25, 22, 598565, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='P6j3WiAvVFMsKB7', max_length=15),
        ),
        migrations.AlterField(
            model_name='withdrawals',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobada', 'Aprobada'), ('Rechazada', 'Rechazada')], default='Pendiente', max_length=50),
        ),
    ]