# Generated by Django 4.2.5 on 2023-10-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisptransaction',
            name='transRef',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fisptransaction',
            name='isDeposited',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
