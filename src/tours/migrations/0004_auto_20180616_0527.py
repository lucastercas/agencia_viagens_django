# Generated by Django 2.0.4 on 2018-06-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20180616_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='value_adult',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tour',
            name='value_children',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
