# Generated by Django 5.0.2 on 2024-03-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('tname', models.CharField(max_length=20)),
                ('p', models.IntegerField()),
                ('w', models.IntegerField()),
                ('l', models.IntegerField()),
                ('d', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
