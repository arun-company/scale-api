# Generated by Django 2.0.3 on 2018-03-22 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_auto_20180322_0400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weight',
            old_name='mearsured',
            new_name='measured',
        ),
    ]
