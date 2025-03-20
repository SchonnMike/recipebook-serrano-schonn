# Generated by Django 5.1.6 on 2025-03-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyNewTable',
            fields=[
                ('custom_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('remarks', models.CharField(default='', max_length=50)),
                ('otherRemarks', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
