# Generated by Django 4.2.4 on 2023-08-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('deleted', 'Deleted'), ('active', 'Active'), ('waitingapproval', 'Waiting approval')], default='active', max_length=50),
        ),
    ]
