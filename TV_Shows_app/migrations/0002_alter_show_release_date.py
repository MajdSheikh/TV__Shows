# Generated by Django 4.1.1 on 2022-09-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TV_Shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
