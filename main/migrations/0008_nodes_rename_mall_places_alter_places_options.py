# Generated by Django 4.0 on 2022-05-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_mall_addr_housenumber_alter_mall_addr_street_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.TextField(default='None', primary_key=True, serialize=False, verbose_name='Node id')),
                ('place_name', models.TextField(default='None', verbose_name='Place name')),
                ('node_geometry', models.TextField(default='None', verbose_name='Coordinates')),
            ],
            options={
                'verbose_name': 'Node',
                'verbose_name_plural': 'Nodes',
            },
        ),
        migrations.RenameModel(
            old_name='Mall',
            new_name='Places',
        ),
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
    ]