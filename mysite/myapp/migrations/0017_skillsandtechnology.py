# Generated by Django 2.0.10 on 2019-02-18 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0016_auto_20190218_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsAndTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologies', models.CharField(default='', max_length=300)),
                ('servers', models.CharField(default='', max_length=300)),
                ('databases', models.CharField(default='', max_length=300)),
                ('other', models.CharField(default='', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
