# Generated by Django 3.0 on 2019-12-06 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'campaign',
                'verbose_name_plural': 'campaigns',
            },
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'data source',
                'verbose_name_plural': 'data sources',
            },
        ),
        migrations.CreateModel(
            name='CampaignStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('clicks', models.IntegerField(verbose_name='clicks')),
                ('impressions', models.IntegerField(verbose_name='impressions')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Campaign')),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.DataSource')),
            ],
            options={
                'verbose_name': 'campaign stats',
                'verbose_name_plural': 'campaign stats',
                'unique_together': {('date', 'data_source', 'campaign')},
            },
        ),
    ]