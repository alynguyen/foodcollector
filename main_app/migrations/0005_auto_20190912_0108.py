# Generated by Django 2.2.3 on 2019-09-12 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190911_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['-name']},
        ),
    ]
