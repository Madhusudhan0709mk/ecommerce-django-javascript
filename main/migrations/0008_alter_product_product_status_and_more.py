# Generated by Django 5.0.4 on 2024-05-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_product_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('disabled', 'Disabled'), ('in_review', 'In_review'), ('draft', 'Draft'), ('rejected', 'Rejected')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(5, '★★★★★'), (1, '★☆☆☆☆'), (4, '★★★★☆'), (2, '★★☆☆☆'), (3, '★★★☆☆')], default=None),
        ),
    ]
