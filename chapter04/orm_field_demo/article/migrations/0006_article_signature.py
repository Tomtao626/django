# Generated by Django 2.0 on 2020-11-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20201124_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='signature',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
