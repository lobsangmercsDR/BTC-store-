# Generated by Django 4.1.7 on 2023-05-27 18:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0027_product_description_product_image_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.subcategory'),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 18, 25, 32, 486974, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitationcodes',
            name='invitationCodes',
            field=models.CharField(default='DlDg0rfIpmKQaaC', max_length=15),
        ),
    ]