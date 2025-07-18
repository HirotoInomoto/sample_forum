# Generated by Django 5.2.4 on 2025-07-05 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='トピック名')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topic')),
            ],
        ),
    ]
