# Generated by Django 5.0.3 on 2024-03-11 00:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boxes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=20)),
            ],
            options={
                'db_table': 'coins',
            },
        ),
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'balance',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('credited', 'Credited'), ('debited', 'Debited')], max_length=20)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxes.box')),
            ],
            options={
                'db_table': 'operations',
            },
        ),
    ]