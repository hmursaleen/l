# Generated by Django 4.2.4 on 2023-08-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('waitingapproval', 'Waiting approval'), ('draft', 'Draft'), ('deleted', 'Deleted'), ('active', 'Active')], default='active', max_length=50),
        ),
    ]
