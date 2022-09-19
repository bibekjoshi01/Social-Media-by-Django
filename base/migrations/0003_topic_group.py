# Generated by Django 4.0.5 on 2022-07-14 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_profile_pic_alter_user_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_photo', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topic')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
