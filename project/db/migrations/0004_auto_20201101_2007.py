# Generated by Django 3.1.2 on 2020-11-01 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20201029_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+2348105110615', max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='avatar_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='firstname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='lastname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
