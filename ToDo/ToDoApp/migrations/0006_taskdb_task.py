# Generated by Django 5.0.6 on 2024-05-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0005_taskdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskdb',
            name='Task',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
