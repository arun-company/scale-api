# Generated by Django 2.0.3 on 2018-04-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0017_auto_20180405_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='measured',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='measurement_date',
            field=models.DateTimeField(),
        ),
    ]