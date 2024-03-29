# Generated by Django 5.0.1 on 2024-02-10 06:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_classroom_options_classroom_created_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='participants',
            field=models.ManyToManyField(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), null=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
