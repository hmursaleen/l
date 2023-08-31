# Generated by Django 4.2.4 on 2023-08-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='average_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted'), ('draft', 'Draft'), ('waitingapproval', 'Waiting approval')], default='active', max_length=50),
        ),
    ]
