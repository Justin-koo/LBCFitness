# Generated by Django 5.0.6 on 2024-08-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_paymentlog_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentlog',
            name='membership_type',
            field=models.CharField(choices=[('new', 'New'), ('extended', 'Extended')], default='new', max_length=10),
        ),
    ]
