# Generated by Django 4.0.2 on 2022-02-13 11:17

import IzoorD.mssql_uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', IzoorD.mssql_uuid.MssqlUUID(default=None, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
            options={
                'db_table': 'testing',
            },
        ),
    ]