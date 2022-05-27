# Generated by Django 4.0 on 2022-05-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_product_alter_shop_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mall_id',
        ),
        migrations.AddField(
            model_name='product',
            name='shop_id',
            field=models.IntegerField(default=1, verbose_name='Shop id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.TextField(max_length=25555, unique=True, verbose_name='Product image link'),
        ),
    ]
