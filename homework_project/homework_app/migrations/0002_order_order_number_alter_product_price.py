# Generated by Django 5.0.2 on 2024-02-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
