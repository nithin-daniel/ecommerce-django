# Generated by Django 4.2.4 on 2023-08-29 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cartitem_price_cartitem_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='payment_id',
        ),
    ]
