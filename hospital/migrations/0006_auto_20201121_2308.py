# Generated by Django 3.1.3 on 2020-11-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_healthdetails_dry_cough'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthdetails',
            name='aches',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='chest_pain',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='conjunctivitis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='diarrhoea',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='headache',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='loss_of_speech',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='loss_of_taste_or_smell',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='rash',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='shortness_of_breath',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='sore_throat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthdetails',
            name='tiredness',
            field=models.BooleanField(default=False),
        ),
    ]
