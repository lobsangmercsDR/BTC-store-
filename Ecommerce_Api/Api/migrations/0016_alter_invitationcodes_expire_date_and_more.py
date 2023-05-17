# Generated by Django 4.1.7 on 2023-04-26 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0015_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 0, 42, 43, 333153, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='jYOhd8NqR1vS0Ay', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dateReleased',
            field=models.DateField(auto_now_add=True),
        ),
    ]