# Generated by Django 2.0.3 on 2018-03-22 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_account_acc_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acc_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='app',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='carrier',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='client_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='homedir',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='account_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='client_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='accountprofile',
            name='value',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='family_id',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='family_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='account_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='client_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secret',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secret_email',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secret_pw',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weight',
            name='account',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='account_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='client_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='device_id',
            field=models.CharField(blank=True, default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='device_sn',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='member_id',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='remark',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='weightrecord',
            name='utc',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
