# Generated by Django 5.0.4 on 2024-04-27 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_vendor_alter_cartorder_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='product_status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('delivered', 'Delivered'), ('process', 'Processing')], default='processing', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('draft', 'Draft'), ('disabled', 'Disabled'), ('in_review', 'In_review')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(3, '★★★☆☆'), (5, '★★★★★'), (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (4, '★★★★☆')], default=None),
        ),
    ]