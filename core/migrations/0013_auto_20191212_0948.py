# Generated by Django 3.0 on 2019-12-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_customuser_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='address',
        ),
        migrations.AddField(
            model_name='incident',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
