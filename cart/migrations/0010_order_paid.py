# Generated by Django 4.2.4 on 2023-09-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
