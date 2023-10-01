# Generated by Django 4.1.7 on 2023-08-02 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0084_rename_nameproduct_productfisic_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='methodproducts',
            old_name='nameProduct',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 20, 17, 22, 65412, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='tuB20OXlkSBi8yp', max_length=15),
        ),
    ]