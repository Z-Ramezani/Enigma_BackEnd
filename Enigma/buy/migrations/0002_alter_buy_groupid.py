# Generated by Django 4.1.4 on 2023-04-11 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0001_initial'),
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupID_id', to='Group.group'),
        ),
    ]