# Generated by Django 5.1.6 on 2025-03-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0012_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(default='Unknown', max_length=50),
        ),
    ]
