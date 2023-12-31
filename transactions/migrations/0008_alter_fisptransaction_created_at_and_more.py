# Generated by Django 4.2.5 on 2023-10-04 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_fisptransaction_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisptransaction',
            name='created_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='fisptransaction',
            name='transRef',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
    ]
