# Generated by Django 3.1.3 on 2020-11-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_healthdetails_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(default='1997-02-09'),
            preserve_default=False,
        ),
    ]
