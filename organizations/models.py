from django.urls import reverse

from IzoorD.mssql_uuid import MssqlUUID
from django.db import models


class Organization(models.Model):
    slug = MssqlUUID(primary_key=True, db_column='OrganizationID', max_length=36, editable=False,
                     default=None)
    org_name = models.CharField(db_column='Org_Name', unique=True, max_length=200,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', verbose_name='Name')
    org_address = models.CharField(db_column='Org_Address', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True, verbose_name='Address')
    org_phone1 = models.CharField(db_column='Org_Phone1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True, verbose_name='Phone number')
    org_contact = models.CharField(db_column='Org_Contact', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True, verbose_name='Contact person')
    org_mail = models.CharField(db_column='Org_Mail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True, verbose_name='E-Mail')
    org_web = models.CharField(db_column='Org_Web', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True, verbose_name='WWW')
    org_country = models.CharField(db_column='Org_Country', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True, verbose_name='Country')
    canoverdraft = models.BooleanField(db_column='CanOverdraft', null=True, verbose_name='Unlimited overdraft')
    nowbalanse = models.DecimalField(db_column='NowBalanse', max_digits=19, decimal_places=4, blank=True,
                                     null=True)
    maxoverdraft = models.DecimalField(db_column='MaxOverdraft', max_digits=19, decimal_places=4, blank=True,
                                       null=True)
    responseperson = models.CharField(db_column='ResponsePerson', max_length=30,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True, verbose_name='Response Person')

    def get_absolute_url(self):
        return reverse('org_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.org_name

    def get_countries(self):
        return self.org_country

    class Meta:
        managed = False
        db_table = 'Organization'
        ordering = ['org_name']
