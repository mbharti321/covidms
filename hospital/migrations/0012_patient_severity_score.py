# Generated by Django 3.1.3 on 2020-11-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_auto_20201122_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='severity_score',
            field=models.IntegerField(default=0),
        ),
    ]
