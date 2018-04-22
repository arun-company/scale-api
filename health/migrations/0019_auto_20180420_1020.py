# Generated by Django 2.0.3 on 2018-04-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0018_auto_20180406_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ('created',), 'verbose_name': 'Familie'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('created',), 'verbose_name': 'Member'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to='profile/'),
        ),
    ]
