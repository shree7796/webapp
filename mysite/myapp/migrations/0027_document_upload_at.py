# Generated by Django 2.0.10 on 2019-03-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20190311_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Upload_at',
            field=models.DateField(auto_now=True),
        ),
    ]