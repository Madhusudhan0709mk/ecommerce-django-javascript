# Generated by Django 5.0.4 on 2024-04-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_cartorder_product_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorder',
            options={},
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In_review'), ('draft', 'Draft')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(2, '★★☆☆☆'), (3, '★★★☆☆'), (1, '★☆☆☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None),
        ),
    ]
