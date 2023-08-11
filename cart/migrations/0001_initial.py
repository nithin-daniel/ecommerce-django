# Generated by Django 4.2.4 on 2023-08-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='media/no-image-default.png', upload_to='cart_image/')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]