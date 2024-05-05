# Generated by Django 5.0.4 on 2024-05-01 04:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_cartorderitems_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorderitems',
            name='order',
        ),
        migrations.AddField(
            model_name='cartorderitems',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('in_review', 'In_review'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('draft', 'Draft')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (4, '★★★★☆'), (2, '★★☆☆☆'), (5, '★★★★★'), (3, '★★★☆☆')], default=None),
        ),
        migrations.DeleteModel(
            name='CartOrder',
        ),
    ]
