# Generated by Django 2.0.10 on 2019-03-28 07:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_documentdatainjsonfile_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdatainjsonfile',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]