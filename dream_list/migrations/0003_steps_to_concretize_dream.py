# Generated by Django 5.0.2 on 2024-02-26 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dream_list', '0002_alter_list_of_dream_dream_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps_to_concretize',
            name='dream',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dream_list.list_of_dream'),
        ),
    ]