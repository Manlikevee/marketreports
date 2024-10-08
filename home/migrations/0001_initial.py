# Generated by Django 4.2.16 on 2024-09-05 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='market_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_class', models.CharField(blank=True, max_length=255, null=True)),
                ('product_data', models.JSONField(blank=True, default=list, null=True)),
                ('as_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
