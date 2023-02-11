# Generated by Django 4.0.3 on 2023-02-01 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebs', '0011_product_product_active'),
        ('product', '0003_productoperationsinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecificationsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_abv', models.DecimalField(blank=True, decimal_places=1, default=5.5, max_digits=3, null=True)),
                ('product_srm', models.IntegerField(blank=True, default=5, null=True)),
                ('product_turbidity', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(blank=True, limit_choices_to={'ownership_id': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ebs.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterialsAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_qty', models.CharField(max_length=25, null=True, verbose_name='Quantity')),
                ('material_phase', models.CharField(choices=[('MSH', 'Mash'), ('HSD', 'Hotside'), ('CSD', 'Coldside')], default='MSH', max_length=3)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ebs.material')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ebs.product')),
            ],
        ),
    ]