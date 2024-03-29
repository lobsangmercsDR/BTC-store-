# Generated by Django 4.2.3 on 2023-08-25 18:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0096_remove_productfisic_seller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 18, 58, 36, 130812, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='iNSdgfT69ruEVS9', max_length=15),
        ),
        migrations.CreateModel(
            name='Deposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_orden', models.IntegerField()),
                ('tasaDepositMoment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantityUSD', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
