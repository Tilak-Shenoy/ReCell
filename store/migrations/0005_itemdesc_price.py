# Generated by Django 2.1.3 on 2018-11-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_inventory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdesc',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
