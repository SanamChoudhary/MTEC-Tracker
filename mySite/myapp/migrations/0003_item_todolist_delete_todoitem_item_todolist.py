# Generated by Django 5.1.1 on 2024-09-24 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_todoitem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.AddField(
            model_name='item',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.todolist'),
        ),
    ]
