# Generated by Django 3.1.7 on 2021-03-18 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210318_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='webiste',
            new_name='website',
        ),
    ]
