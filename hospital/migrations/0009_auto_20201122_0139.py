# Generated by Django 3.1.3 on 2020-11-21 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_patient_severity'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='recovery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='severity',
            field=models.IntegerField(choices=[(0, 'Mild'), (1, 'Potenitally worsening'), (2, 'Moderate severity'), (3, 'High severity'), (4, 'Requires urgent care')], default=1),
        ),
    ]
