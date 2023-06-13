# Generated by Django 4.2 on 2023-06-13 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0042_rename_name_productdigit_namestore_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdigit',
            old_name='nameStore',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='stores',
            old_name='name',
            new_name='nameStore',
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 4, 26, 58, 499802, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='8FvNCIIFmKyFuNS', max_length=15),
        ),
    ]