# Generated by Django 3.1.5 on 2021-10-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20211026_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='territory',
            name='territory_code',
            field=models.CharField(default='TERR', max_length=5),
        ),
    ]
