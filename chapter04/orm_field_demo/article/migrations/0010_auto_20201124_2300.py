# Generated by Django 2.0 on 2020-11-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_author_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
