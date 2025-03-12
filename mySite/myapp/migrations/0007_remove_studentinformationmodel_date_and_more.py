# Generated by Django 5.1.1 on 2025-03-11 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_studentinformationmodel_hours_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinformationmodel',
            name='date',
        ),
        migrations.AddField(
            model_name='studentinformationmodel',
            name='cleanup',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='myapp.dateofcleanup'),
        ),
        migrations.AlterField(
            model_name='dateofcleanup',
            name='date',
            field=models.DateField(),
        ),
    ]
