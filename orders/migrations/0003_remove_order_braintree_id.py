# Generated by Django 3.0.1 on 2021-05-18 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='braintree_id',
        ),
    ]