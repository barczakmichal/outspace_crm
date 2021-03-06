# Generated by Django 3.1.7 on 2021-03-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('full_name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('tax_number', models.SmallIntegerField(unique=True)),
                ('industry', models.CharField(max_length=64)),
                ('webiste', models.CharField(max_length=64)),
                ('source_lead', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=64)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('notes', models.CharField(max_length=64)),
            ],
        ),
    ]
