# Generated by Django 2.1.4 on 2019-01-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190122_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
