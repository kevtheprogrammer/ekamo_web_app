# Generated by Django 4.2.5 on 2023-10-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_agentprofile_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agents_to_manage',
            field=models.ManyToManyField(related_name='my_agents', to='account.agentprofile', verbose_name='My Agents'),
        ),
    ]
