# Generated by Django 5.0.1 on 2024-02-04 15:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_classroom_options_classroom_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.classroom'),
            preserve_default=False,
        ),
    ]