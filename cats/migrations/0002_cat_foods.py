# Generated by Django 3.1.4 on 2021-07-09 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='foods',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
