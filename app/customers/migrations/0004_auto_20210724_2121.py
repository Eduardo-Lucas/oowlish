# Generated by Django 3.2.4 on 2021-07-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
