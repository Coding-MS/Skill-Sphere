# Generated by Django 4.2.7 on 2023-11-30 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('note', djrichtextfield.models.RichTextField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('due_date', models.DateField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='task_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
