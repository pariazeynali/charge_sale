# Generated by Django 4.2.3 on 2023-07-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='credit',
            field=models.IntegerField(),
        ),
    ]