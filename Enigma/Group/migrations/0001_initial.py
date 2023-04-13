# Generated by Django 4.1.7 on 2023-04-08 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('currency', models.CharField(default='تومان', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='Group.group')),
            ],
        ),
    ]
