# Generated by Django 4.2.4 on 2023-08-21 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartitem_cart_alter_cartitem_price_ht'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='price_ht',
            new_name='price',
        ),
    ]
