# Generated by Django 4.0.7 on 2022-08-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]