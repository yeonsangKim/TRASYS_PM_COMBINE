# Generated by Django 3.2.8 on 2021-11-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mon_avg', models.FloatField(blank=True, null=True)),
                ('tus_avg', models.FloatField(blank=True, null=True)),
                ('wed_avg', models.FloatField(blank=True, null=True)),
                ('thr_avg', models.FloatField(blank=True, null=True)),
                ('fri_avg', models.FloatField(blank=True, null=True)),
                ('sat_avg', models.FloatField(blank=True, null=True)),
                ('sun_avg', models.FloatField(blank=True, null=True)),
                ('ja', models.IntegerField(blank=True, null=True)),
                ('fe', models.IntegerField(blank=True, null=True)),
                ('mar', models.IntegerField(blank=True, null=True)),
                ('apr', models.IntegerField(blank=True, null=True)),
                ('may', models.IntegerField(blank=True, null=True)),
                ('jun', models.IntegerField(blank=True, null=True)),
                ('jul', models.IntegerField(blank=True, null=True)),
                ('aug', models.IntegerField(blank=True, null=True)),
                ('sep', models.IntegerField(blank=True, null=True)),
                ('oct', models.IntegerField(blank=True, null=True)),
                ('nov', models.IntegerField(blank=True, null=True)),
                ('dec', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usage',
                'managed': False,
            },
        ),
    ]
