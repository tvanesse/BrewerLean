# Generated by Django 4.0.3 on 2023-01-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebs', '0010_alter_product_options_partner_partner_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_active',
            field=models.BooleanField(default=True),
        ),
    ]
