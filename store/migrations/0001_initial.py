# Generated by Django 5.0.4 on 2024-07-10 05:39

import django.db.models.deletion
import django.utils.timezone
import store.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('business_name', models.CharField(max_length=255)),
                ('registration_name', models.CharField(max_length=255)),
                ('ruc', models.BigIntegerField(unique=True, validators=[store.validators.validate_eleven_digits])),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.categories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('business_name', models.CharField(max_length=255)),
                ('registration_name', models.CharField(max_length=255)),
                ('gtin_type', models.CharField(choices=[('EAN8', 'EAN8'), ('EAN13', 'EAN13'), ('LOCAL', 'LOCAL')], default='EAN13', max_length=7)),
                ('gtin', models.BigIntegerField()),
                ('categories', models.ManyToManyField(blank=True, to='store.categories')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.companies')),
            ],
            options={
                'unique_together': {('gtin_type', 'gtin')},
            },
        ),
    ]
