# Generated by Django 5.0.1 on 2024-02-04 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_classroom_updated_alter_message_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={},
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='created',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='message',
            name='created',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated',
        ),
    ]
