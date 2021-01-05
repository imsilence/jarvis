# Generated by Django 3.1.5 on 2021-01-05 11:04

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(default='', error_messages={'unique': 'error.account.user.username.unique'}, help_text='help.account.user.username', max_length=128, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='account.user.username')),
                ('nickname', models.CharField(default='', max_length=128, verbose_name='account.user.nickname')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='account.user.email')),
                ('telephone', models.CharField(blank=True, default='', max_length=32, verbose_name='account.user.telephone')),
                ('is_staff', models.BooleanField(default=False, help_text='help.account.user.is_staff', verbose_name='account.user.is_staff')),
                ('is_active', models.BooleanField(default=True, help_text='help.acount.user.is_active', verbose_name='account.user.is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='account.user.created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='account.user.updated_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='account.user.deleted_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'account.user',
                'verbose_name_plural': 'account.users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
