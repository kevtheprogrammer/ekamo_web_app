# Generated by Django 4.2.5 on 2023-10-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_agentexpenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisptransaction',
            name='transRef',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
