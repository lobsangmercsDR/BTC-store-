# Generated by Django 4.2 on 2023-09-08 00:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0100_gendata_price_checker_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stores',
            old_name='nameStore',
            new_name='name',
        ),
        migrations.AddField(
            model_name='stores',
            name='avatar_img',
            field=models.ImageField(null=True, upload_to='images/store/HerENS.jpg'),
        ),
        migrations.AddField(
            model_name='stores',
            name='banner_img',
            field=models.ImageField(null=True, upload_to='images/store/NysIFT.jpg'),
        ),
        migrations.AddField(
            model_name='stores',
            name='description',
            field=models.CharField(default='description', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 15, 0, 6, 58, 404135, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='pbT5GXttP01K3pm', max_length=15),
        ),
    ]
