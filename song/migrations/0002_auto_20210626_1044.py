# Generated by Django 3.2.4 on 2021-06-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]