# Generated by Django 3.1.5 on 2021-02-04 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebs', '0017_auto_20210204_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='qty_brew_days',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True, verbose_name='Number of Brew Days'),
        ),
    ]
