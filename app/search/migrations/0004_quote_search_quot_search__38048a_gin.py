# Generated by Django 4.1.4 on 2023-03-24 07:38

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_search_vector_trigger'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='quote',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='search_quot_search__38048a_gin'),
        ),
    ]
