# Generated by Django 5.0.2 on 2024-02-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_app', '0005_product_image_alter_order_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='./media'),
        ),
    ]
