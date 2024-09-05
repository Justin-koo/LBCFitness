# Generated by Django 5.0.6 on 2024-08-01 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_paymentlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentlog',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_logs', to='main.member'),
        ),
    ]
