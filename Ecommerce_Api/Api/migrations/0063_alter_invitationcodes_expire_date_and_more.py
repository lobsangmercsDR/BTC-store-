# Generated by Django 4.1.7 on 2023-06-22 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0062_productdigit_needchecker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 29, 19, 59, 49, 310696, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='fnxn431KExMlgcY', max_length=15),
        ),
        migrations.AlterField(
            model_name='productdigit',
            name='needChecker',
            field=models.BooleanField(default=True),
        ),
    ]