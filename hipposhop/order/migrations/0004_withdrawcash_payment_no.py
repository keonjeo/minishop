# Generated by Django 2.0.6 on 2018-07-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180630_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawcash',
            name='payment_no',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='微信流水号'),
        ),
    ]
