# Generated by Django 5.0.4 on 2024-04-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]