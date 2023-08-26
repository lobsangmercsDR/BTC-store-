# Generated by Django 4.2.3 on 2023-08-26 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0097_alter_invitationcodes_expire_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 2, 14, 7, 23, 770002, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='tDjgzyCxdIVadOc', max_length=15),
        ),
        migrations.DeleteModel(
            name='RoleRequests',
        ),
    ]