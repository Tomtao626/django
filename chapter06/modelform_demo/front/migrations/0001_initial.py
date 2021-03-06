# Generated by Django 2.0 on 2021-01-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('page', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': '图书',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('telephone', models.CharField(max_length=11)),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
            },
        ),
    ]
