# Generated by Django 4.0.2 on 2022-03-05 04:37

import IzoorD.mssql_uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_testing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organizationid', IzoorD.mssql_uuid.MssqlUUID(db_column='OrganizationID', default=None, editable=False, primary_key=True, serialize=False)),
                ('org_name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Name', max_length=200, null=True, unique=True)),
                ('org_address', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Address', max_length=200, null=True)),
                ('org_phone1', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Phone1', max_length=20, null=True)),
                ('org_contact', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Contact', max_length=100, null=True)),
                ('org_mail', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Mail', max_length=100, null=True)),
                ('org_web', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Web', max_length=50, null=True)),
                ('org_country', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Org_Country', max_length=20, null=True)),
                ('canoverdraft', models.BooleanField(db_column='CanOverdraft', null=True)),
                ('nowbalanse', models.DecimalField(blank=True, db_column='NowBalanse', decimal_places=4, max_digits=19, null=True)),
                ('maxoverdraft', models.DecimalField(blank=True, db_column='MaxOverdraft', decimal_places=4, max_digits=19, null=True)),
                ('responseperson', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ResponsePerson', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Organization',
                'managed': False,
            },
        ),
    ]
