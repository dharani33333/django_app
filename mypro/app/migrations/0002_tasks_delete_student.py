# Generated by Django 5.2 on 2025-05-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=40)),
                ('description', models.TextField(default='')),
                ('created_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
