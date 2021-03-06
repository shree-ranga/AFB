# Generated by Django 3.2.9 on 2021-11-12 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('due_date', models.DateField()),
                ('labels', models.CharField(blank=True, max_length=30)),
                ('priority', models.CharField(blank=True, choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=6)),
                ('completed', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
