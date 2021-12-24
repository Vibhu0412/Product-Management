# Generated by Django 4.0 on 2021-12-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_tag_remove_product_is_published_remove_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(default=False, null=True, to='products.Tag'),
        ),
    ]