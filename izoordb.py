# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actinvent(models.Model):
    actinventid = models.CharField(db_column='ActInventId', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    actdatetime = models.DateTimeField(db_column='ActDateTime', blank=True, null=True)  # Field name made lowercase.
    actstatus = models.CharField(db_column='ActStatus', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actinvent'


class Agentreward(models.Model):
    agentrewardid = models.CharField(db_column='AgentRewardId', primary_key=True, max_length=36)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    kass_doc_id = models.CharField(db_column='Kass_doc_id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    online_doc_id = models.CharField(db_column='OnLine_Doc_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True)  # Field name made lowercase.
    tax_out = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    agentrewardmainid = models.CharField(db_column='AgentRewardMainId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgentReward'


class Agentrewardmain(models.Model):
    agentrewardmainid = models.CharField(db_column='AgentRewardMainId', primary_key=True, max_length=36)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.CharField(db_column='Doc_num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True)  # Field name made lowercase.
    totalcommis = models.DecimalField(db_column='TotalCommis', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tax_out = models.DecimalField(db_column='Tax_Out', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgentRewardMain'


class Agents(models.Model):
    agentid = models.CharField(db_column='AgentId', primary_key=True, max_length=36)  # Field name made lowercase.
    agent_name = models.CharField(db_column='Agent_Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_izoorid = models.CharField(db_column='Agent_IZOORID', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_photo = models.BinaryField(db_column='Agent_Photo', blank=True, null=True)  # Field name made lowercase.
    agent_email = models.CharField(db_column='Agent_Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_phone = models.CharField(db_column='Agent_Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_phone2 = models.CharField(db_column='Agent_Phone2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_address = models.CharField(db_column='Agent_Address', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_nicname = models.CharField(db_column='Agent_NicName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_comments = models.CharField(db_column='Agent_Comments', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_thai_id = models.CharField(db_column='Agent_Thai_Id', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_status = models.CharField(db_column='Agent_Status', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_level = models.CharField(db_column='Agent_Level', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_postcode = models.CharField(db_column='Agent_PostCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_city = models.CharField(db_column='Agent_City', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_country = models.CharField(db_column='Agent_Country', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agent_bank_account = models.CharField(db_column='Agent_Bank_Account', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agents'


class Ankets2Annual(models.Model):
    crossid = models.CharField(db_column='CrossID', primary_key=True, max_length=36)  # Field name made lowercase.
    annualid = models.CharField(db_column='AnnualId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    guest_id = models.CharField(db_column='Guest_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wrist_type = models.CharField(db_column='Wrist_Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ankets2Annual'


class Annual(models.Model):
    annualid = models.CharField(db_column='AnnualId', primary_key=True, max_length=36)  # Field name made lowercase.
    annualnum = models.CharField(db_column='AnnualNum', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualdatesale = models.DateTimeField(db_column='AnnualDateSale', blank=True, null=True)  # Field name made lowercase.
    annualdateexpired = models.DateTimeField(db_column='AnnualDateExpired', blank=True, null=True)  # Field name made lowercase.
    annualtype = models.CharField(db_column='AnnualType', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualname = models.CharField(db_column='AnnualName', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualstatus = models.CharField(db_column='AnnualStatus', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualcomment = models.CharField(db_column='AnnualComment', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualemail = models.CharField(db_column='AnnualEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualphone = models.CharField(db_column='AnnualPhone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualaddress = models.CharField(db_column='AnnualAddress', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualnickname = models.CharField(db_column='AnnualNickName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualidcustomer = models.CharField(db_column='AnnualIdCustomer', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    annualphoto = models.BinaryField(db_column='AnnualPhoto', blank=True, null=True)  # Field name made lowercase.
    annualbirthday = models.DateTimeField(db_column='AnnualBirthday', blank=True, null=True)  # Field name made lowercase.
    annualprice = models.DecimalField(db_column='AnnualPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Annual'


class Aspnetroles(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetRoles'


class Aspnetuserclaims(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserClaims'


class Aspnetuserlogins(models.Model):
    loginprovider = models.CharField(db_column='LoginProvider', primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    providerkey = models.CharField(db_column='ProviderKey', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserLogins'
        unique_together = (('loginprovider', 'providerkey', 'userid'),)


class Aspnetuserroles(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey(Aspnetroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserRoles'
        unique_together = (('userid', 'roleid'),)


class Aspnetusers(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailconfirmed = models.BooleanField(db_column='EmailConfirmed')  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.TextField(db_column='SecurityStamp', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonenumberconfirmed = models.BooleanField(db_column='PhoneNumberConfirmed')  # Field name made lowercase.
    twofactorenabled = models.BooleanField(db_column='TwoFactorEnabled')  # Field name made lowercase.
    lockoutenddateutc = models.DateTimeField(db_column='LockoutEndDateUtc', blank=True, null=True)  # Field name made lowercase.
    lockoutenabled = models.BooleanField(db_column='LockoutEnabled')  # Field name made lowercase.
    accessfailedcount = models.IntegerField(db_column='AccessFailedCount')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUsers'


class Cabanaevent(models.Model):
    cabanaeventid = models.CharField(db_column='CabanaEventId', primary_key=True, max_length=36)  # Field name made lowercase.
    cabanastateid = models.CharField(db_column='CabanaStateId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    cabanaeventdate = models.DateTimeField(db_column='CabanaEventDate', blank=True, null=True)  # Field name made lowercase.
    cabanaeventdescription = models.CharField(db_column='CabanaEventDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CabanaEvent'


class Cabanastate(models.Model):
    cabanastateid = models.CharField(db_column='CabanaStateId', primary_key=True, max_length=36)  # Field name made lowercase.
    cabanaid = models.CharField(db_column='CabanaId', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cabanastatus = models.CharField(db_column='CabanaStatus', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statusdate = models.DateTimeField(db_column='StatusDate', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recieptnum = models.CharField(db_column='RecieptNum', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reciepttype = models.CharField(db_column='RecieptType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statusdateto = models.DateTimeField(db_column='StatusDateTo', blank=True, null=True)  # Field name made lowercase.
    cabana_depo = models.DecimalField(db_column='Cabana_Depo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    recieptdeporet = models.CharField(db_column='RecieptDepoRet', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bookingdate = models.DateTimeField(db_column='BookingDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CabanaState'


class Cabanas(models.Model):
    cabanaid = models.CharField(db_column='CabanaID', primary_key=True, max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cabanaplaces = models.IntegerField(db_column='CabanaPlaces', blank=True, null=True)  # Field name made lowercase.
    cabanaprice = models.DecimalField(db_column='CabanaPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cabanastatus = models.CharField(db_column='CabanaStatus', max_length=19, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    code_workplace = models.CharField(db_column='Code_workplace', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cabanapict = models.CharField(db_column='CabanaPict', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cabanawidth = models.IntegerField(db_column='CabanaWidth', blank=True, null=True)  # Field name made lowercase.
    cabanaheight = models.IntegerField(db_column='Cabanaheight', blank=True, null=True)  # Field name made lowercase.
    cabanax0 = models.IntegerField(db_column='CabanaX0', blank=True, null=True)  # Field name made lowercase.
    cabanay0 = models.IntegerField(db_column='CabanaY0', blank=True, null=True)  # Field name made lowercase.
    icon_free = models.BinaryField(db_column='Icon_Free', blank=True, null=True)  # Field name made lowercase.
    icon_busy = models.BinaryField(db_column='Icon_Busy', blank=True, null=True)  # Field name made lowercase.
    cabanaphoto = models.BinaryField(db_column='CabanaPhoto', blank=True, null=True)  # Field name made lowercase.
    cod_skdk = models.CharField(db_column='COD_SKDK', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cabana_depo = models.DecimalField(db_column='Cabana_Depo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cabanas'


class CabanasZone(models.Model):
    zone_id = models.CharField(db_column='Zone_id', primary_key=True, max_length=36)  # Field name made lowercase.
    zone_name = models.CharField(db_column='Zone_name', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zone_pict = models.BinaryField(db_column='Zone_Pict', blank=True, null=True)  # Field name made lowercase.
    zone_x0 = models.IntegerField(db_column='Zone_X0', blank=True, null=True)  # Field name made lowercase.
    zone_y0 = models.IntegerField(db_column='Zone_Y0', blank=True, null=True)  # Field name made lowercase.
    zone_width = models.IntegerField(db_column='Zone_Width', blank=True, null=True)  # Field name made lowercase.
    zone_height = models.IntegerField(db_column='Zone_Height', blank=True, null=True)  # Field name made lowercase.
    zone_order = models.IntegerField(db_column='Zone_order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cabanas_zone'


class Calendar(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    weekid = models.IntegerField(db_column='WeekID', blank=True, null=True)  # Field name made lowercase.
    weekname = models.CharField(db_column='WeekName', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendar'


class Calendarholidays(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    function = models.IntegerField(db_column='Function')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalendarHolidays'
        unique_together = (('date', 'function'),)


class Cod2Scheme(models.Model):
    cod2schemeid = models.CharField(db_column='Cod2SchemeId', primary_key=True, max_length=36)  # Field name made lowercase.
    cod_skdk = models.CharField(db_column='Cod_SKDK', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_scheme_code = models.CharField(db_column='DSC_SCHEME_CODE', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    discount_proc = models.DecimalField(db_column='Discount_Proc', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cod2Scheme'


class Contracts(models.Model):
    contractid = models.CharField(db_column='ContractId', primary_key=True, max_length=36)  # Field name made lowercase.
    contractnum = models.CharField(db_column='ContractNum', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contractdate = models.DateTimeField(db_column='ContractDate', blank=True, null=True)  # Field name made lowercase.
    org_code = models.CharField(db_column='Org_Code', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    catalog_code = models.CharField(db_column='Catalog_Code', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contractdatefrom = models.DateTimeField(db_column='ContractDateFrom', blank=True, null=True)  # Field name made lowercase.
    contractdateto = models.DateTimeField(db_column='ContractDateTo', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=260, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contractname = models.CharField(db_column='ContractName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    orgid = models.CharField(db_column='OrgId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contracts'


class Country(models.Model):
    iso_a3 = models.CharField(db_column='ISO_A3', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    iso_n3 = models.IntegerField(db_column='ISO_N3', unique=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    show = models.CharField(db_column='SHOW', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SORTORDER', blank=True, null=True)  # Field name made lowercase.
    bali_cod_a3 = models.CharField(db_column='Bali_Cod_A3', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bali_cod_n3 = models.IntegerField(db_column='Bali_Cod_N3', blank=True, null=True)  # Field name made lowercase.
    countryid = models.CharField(db_column='CountryId', primary_key=True, max_length=36)  # Field name made lowercase.
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Country'


class Coupons(models.Model):
    couponid = models.CharField(db_column='CouponId', primary_key=True, max_length=36)  # Field name made lowercase.
    couponnumber = models.CharField(db_column='CouponNumber', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kass_oper_id = models.CharField(db_column='Kass_oper_id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    name_item = models.CharField(db_column='Name_item', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    count_item = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price_tot = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    applyingdate = models.DateTimeField(db_column='ApplyingDate', blank=True, null=True)  # Field name made lowercase.
    applyingwristband = models.CharField(db_column='ApplyingWristband', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recdatetime = models.DateTimeField(db_column='Recdatetime', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.TextField(db_column='ItemCode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dateenterfrom = models.DateTimeField(db_column='DateEnterFrom', blank=True, null=True)  # Field name made lowercase.
    dateenteruntil = models.DateTimeField(db_column='DateEnterUntil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coupons'


class Currency(models.Model):
    currencyid = models.CharField(db_column='CurrencyId', primary_key=True, max_length=36)  # Field name made lowercase.
    currencyname = models.CharField(db_column='CurrencyName', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    timeset = models.DateTimeField(db_column='TimeSet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Currency'


class DscScheme(models.Model):
    dsc_scheme_id = models.CharField(db_column='DSC_SCHEME_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    dsc_scheme_code = models.CharField(db_column='DSC_SCHEME_CODE', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_scheme_description = models.CharField(db_column='DSC_SCHEME_Description', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_scheme_script = models.CharField(db_column='DSC_SCHEME_Script', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DSC_SCHEME'


class Defrag(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    db = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    shema = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    table = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    indexname = models.CharField(db_column='IndexName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frag_num = models.IntegerField(blank=True, null=True)
    frag = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    rec = models.IntegerField(blank=True, null=True)
    func = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    tf = models.DateTimeField(blank=True, null=True)
    frag_after = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    idx = models.IntegerField(blank=True, null=True)
    insertutcdate = models.DateTimeField(db_column='InsertUTCDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Defrag'


class Depositcard(models.Model):
    depositcard_id = models.CharField(db_column='DepositCard_ID', max_length=36)  # Field name made lowercase.
    dsc_card_id = models.CharField(db_column='DSC_CARD_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    depositcard_number = models.CharField(db_column='DepositCard_NUMBER', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nowbalanñe = models.DecimalField(db_column='NowBalanñe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maxoverdraft = models.DecimalField(db_column='MaxOverdraft', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    depositcard_name = models.CharField(db_column='DepositCard_Name', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    depositcard_email = models.CharField(db_column='DepositCard_Email', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositCard'


class Dictionary(models.Model):
    phrase_id = models.CharField(db_column='Phrase_Id', primary_key=True, max_length=36)  # Field name made lowercase.
    eng = models.CharField(db_column='Eng', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rus = models.CharField(db_column='Rus', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    thai = models.CharField(db_column='Thai', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chi = models.CharField(db_column='Chi', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kor = models.CharField(db_column='Kor', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    jap = models.CharField(db_column='Jap', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ger = models.CharField(db_column='Ger', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fra = models.CharField(db_column='Fra', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dictionary'


class Discountcard(models.Model):
    dsc_card_id = models.CharField(db_column='DSC_CARD_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    dsc_card_number = models.CharField(db_column='DSC_CARD_NUMBER', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_dat_start = models.DateTimeField(db_column='DSC_Dat_Start', blank=True, null=True)  # Field name made lowercase.
    dsc_dat_end = models.DateTimeField(db_column='DSC_Dat_End', blank=True, null=True)  # Field name made lowercase.
    dsc_email = models.CharField(db_column='DSC_Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_scheme_cod = models.CharField(db_column='DSC_Scheme_cod', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_nickname = models.CharField(db_column='DSC_NickName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_phone = models.CharField(db_column='DSC_Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiscountCard'


class Driver(models.Model):
    driver_guid = models.CharField(db_column='Driver_GUID', primary_key=True, max_length=36)  # Field name made lowercase.
    driver_name = models.CharField(db_column='Driver_Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_izoorid = models.CharField(db_column='Driver_IZOORID', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_photo = models.BinaryField(db_column='Driver_Photo', blank=True, null=True)  # Field name made lowercase.
    driver_email = models.CharField(db_column='Driver_Email', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_phone = models.CharField(db_column='Driver_Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_address = models.CharField(db_column='Driver_Address', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_nicname = models.CharField(db_column='Driver_NicName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_comments = models.CharField(db_column='Driver_Comments', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_thai_id = models.CharField(db_column='Driver_Thai_Id', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_license = models.CharField(db_column='Driver_License', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    driver_car_plate = models.CharField(db_column='Driver_Car_plate', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_car = models.CharField(db_column='Type_Car', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    use_sticker = models.BooleanField(db_column='Use_Sticker', blank=True, null=True)  # Field name made lowercase.
    taxi_id = models.CharField(db_column='Taxi_ID', max_length=17, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    license_expired = models.DateField(db_column='License_Expired', blank=True, null=True)  # Field name made lowercase.
    contract_expired = models.DateField(db_column='Contract_Expired', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Driver'


class Employees(models.Model):
    employeeid = models.CharField(db_column='EmployeeID', unique=True, max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    taxcode = models.CharField(db_column='TaxCode', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employeeguid = models.CharField(db_column='EmployeeGuid', primary_key=True, max_length=36)  # Field name made lowercase.
    dateofentry = models.DateTimeField(db_column='DateOfEntry', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Goodsmove(models.Model):
    goodsmoveid = models.CharField(db_column='GoodsMoveID', primary_key=True, max_length=36)  # Field name made lowercase.
    goodsid = models.CharField(db_column='goodsID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    type_move = models.CharField(db_column='Type_Move', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    movedate = models.DateTimeField(db_column='MoveDate', blank=True, null=True)  # Field name made lowercase.
    movedocnum = models.CharField(db_column='MoveDocNum', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsprice = models.DecimalField(db_column='GoodsPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsqty = models.DecimalField(db_column='GoodsQTY', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    goodsdiscount = models.DecimalField(db_column='GoodsDiscount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodssumm = models.DecimalField(db_column='GoodsSumm', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsvat = models.DecimalField(db_column='GoodsVat', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsfoc = models.SmallIntegerField(db_column='GoodsFOC', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pos_id = models.CharField(db_column='POS_ID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsmovedocid = models.CharField(db_column='GoodsMoveDocId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodsmovetimereg = models.DateTimeField(db_column='GoodsMoveTimeReg', blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    movedocline = models.CharField(db_column='MovedocLine', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodscost = models.DecimalField(db_column='GoodsCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsinputvat = models.DecimalField(db_column='GoodsInputVAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsMove'
        unique_together = (('goodsmovedocid', 'goodsid', 'type_move', 'movedocline'),)


class Goodsmovedoc(models.Model):
    goodsmovedocid = models.CharField(db_column='GoodsMoveDocId', primary_key=True, max_length=36)  # Field name made lowercase.
    goodsmovedoc_date = models.DateTimeField(db_column='GoodsMoveDoc_Date', blank=True, null=True)  # Field name made lowercase.
    goodsmovedoc_num = models.CharField(db_column='GoodsMoveDoc_Num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsmove_type = models.CharField(db_column='GoodsMove_Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    point_from = models.CharField(db_column='Point_From', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    point_to = models.CharField(db_column='Point_To', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsmovedoc_summ = models.DecimalField(db_column='GoodsMoveDoc_Summ', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsMoveDoc'


class Goodsprices(models.Model):
    goodsid = models.CharField(db_column='goodsID', primary_key=True, max_length=36)  # Field name made lowercase.
    goods_code = models.CharField(max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    goods_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    goods_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    goodsphoto = models.BinaryField(db_column='GoodsPhoto', blank=True, null=True)  # Field name made lowercase.
    cod_skdk = models.CharField(db_column='Cod_SKDK', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goods_description = models.CharField(db_column='Goods_Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    internalnumber = models.CharField(db_column='InternalNumber', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goods_categoryid = models.CharField(db_column='Goods_CategoryId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goods_groupid = models.CharField(db_column='Goods_GroupId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=36)  # Field name made lowercase.
    goods_group = models.CharField(db_column='Goods_Group', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goods_subgroup = models.CharField(db_column='Goods_SubGroup', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rest_qty = models.DecimalField(db_column='Rest_QTY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    goods_zones = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name_tran = models.CharField(db_column='Name_Tran', max_length=350, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    price_2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GoodsPrices'
        unique_together = (('goods_code', 'supplierid'),)


class Goodsreciept(models.Model):
    goodsrecieptid = models.CharField(db_column='GoodsRecieptId', primary_key=True, max_length=36)  # Field name made lowercase.
    goodsrecieptnum = models.CharField(db_column='GoodsRecieptNum', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsrecieptdate = models.DateTimeField(db_column='GoodsRecieptDate', blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodsrecieptsumm = models.DecimalField(db_column='GoodsRecieptSumm', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsrecieptcomment = models.CharField(db_column='GoodsRecieptComment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsrecieptvat = models.DecimalField(db_column='GoodsRecieptVAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsreciepturladddoc = models.CharField(db_column='GoodsRecieptUrlAddDoc', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usercreator = models.CharField(db_column='UserCreator', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datecreate = models.DateTimeField(db_column='DateCreate', blank=True, null=True)  # Field name made lowercase.
    userlastedit = models.CharField(db_column='UserLastEdit', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datelastedit = models.DateTimeField(db_column='DateLastEdit', blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    accepted = models.BooleanField(db_column='Accepted', blank=True, null=True)  # Field name made lowercase.
    goodsreciepttype = models.CharField(db_column='GoodsRecieptType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReciept'


class Goodsrest(models.Model):
    goodsrestid = models.CharField(db_column='GoodsRestId', primary_key=True, max_length=36)  # Field name made lowercase.
    goodsid = models.CharField(db_column='GoodsId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    rest_qty = models.DecimalField(db_column='Rest_QTY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='OutLet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ptrinter2coupon = models.CharField(db_column='Ptrinter2Coupon', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hide = models.BooleanField(db_column='Hide', blank=True, null=True)  # Field name made lowercase.
    sortingmenu = models.CharField(db_column='SortingMenu', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    closed = models.BooleanField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsRest'
        unique_together = (('goodsid', 'outlet'),)


class Goodsunits(models.Model):
    id = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GoodsUnits'


class GoodsCategory(models.Model):
    goods_categoryid = models.CharField(db_column='Goods_CategoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    goods_category = models.CharField(db_column='Goods_Category', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goods_categorychar = models.CharField(db_column='Goods_CategoryChar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sorting_number = models.CharField(db_column='Sorting_Number', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Goods_Category'


class GoodsGroup(models.Model):
    goods_groupid = models.CharField(db_column='Goods_GroupId', primary_key=True, max_length=36)  # Field name made lowercase.
    goods_group = models.CharField(db_column='Goods_Group', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goods_groupchar = models.CharField(db_column='Goods_GroupChar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Goods_Group'


class Guestankets(models.Model):
    guest_id = models.CharField(db_column='Guest_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    guestname = models.CharField(db_column='GuestName', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guestemail = models.CharField(db_column='GuestEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guestphone = models.CharField(db_column='GuestPhone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guestaddress = models.CharField(db_column='GuestAddress', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guestnickname = models.CharField(db_column='GuestNickName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guestphoto = models.BinaryField(db_column='GuestPhoto', blank=True, null=True)  # Field name made lowercase.
    guestbirthday = models.DateTimeField(db_column='GuestBirthday', blank=True, null=True)  # Field name made lowercase.
    guestcomment = models.CharField(db_column='GuestComment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(unique=True, blank=True, null=True)
    printnumber = models.CharField(db_column='PrintNumber', max_length=13, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GuestAnkets'


class Ingredient(models.Model):
    ingredientid = models.CharField(db_column='ingredientID', primary_key=True, max_length=36)  # Field name made lowercase.
    goodsidmain = models.CharField(db_column='GoodsIdMain', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodsidadd = models.CharField(db_column='GoodsIdAdd', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredient'


class Invent(models.Model):
    inventid = models.CharField(db_column='InventID', primary_key=True, max_length=36)  # Field name made lowercase.
    goodsid = models.CharField(db_column='GoodsId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    pos_id = models.CharField(db_column='POS_ID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goodsqty = models.DecimalField(db_column='GoodsQTY', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='Rectime', blank=True, null=True)  # Field name made lowercase.
    actnumber = models.CharField(db_column='ActNumber', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rest_qty = models.DecimalField(db_column='Rest_QTY', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invent'


class KassDoc(models.Model):
    kass_doc_id = models.CharField(db_column='Kass_doc_id', primary_key=True, max_length=36)  # Field name made lowercase.
    kass_doc_date = models.DateTimeField(db_column='Kass_doc_Date', blank=True, null=True)  # Field name made lowercase.
    pos_id = models.CharField(db_column='POS_id', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summ_tot = models.DecimalField(db_column='Summ_TOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_cash = models.DecimalField(db_column='Summ_Cash', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_credcard = models.DecimalField(db_column='Summ_CredCard', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kass_doc_num = models.CharField(db_column='Kass_Doc_Num', unique=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summ_by_deposite = models.DecimalField(db_column='Summ_By_Deposite', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    catalog_price = models.CharField(db_column='Catalog_price', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cashier = models.CharField(db_column='Cashier', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reciept_type = models.CharField(db_column='Reciept_Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    n_preschool = models.IntegerField(db_column='N_Preschool', blank=True, null=True)  # Field name made lowercase.
    n_adult = models.IntegerField(db_column='N_Adult', blank=True, null=True)  # Field name made lowercase.
    n_child = models.IntegerField(db_column='N_Child', blank=True, null=True)  # Field name made lowercase.
    n_limited = models.IntegerField(db_column='N_Limited', blank=True, null=True)  # Field name made lowercase.
    contract_id = models.CharField(db_column='Contract_id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    member_id = models.CharField(db_column='Member_id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    annual_id = models.CharField(db_column='Annual_id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    name_outer_base = models.CharField(db_column='Name_Outer_Base', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summ_change = models.DecimalField(db_column='Summ_Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    s_top_up = models.DecimalField(db_column='S_top_up', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    s_top_down = models.DecimalField(db_column='S_top_down', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balans_st = models.DecimalField(db_column='Balans_st', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balans_end = models.DecimalField(db_column='Balans_end', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_depot = models.DecimalField(db_column='Sum_depoT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_depol = models.DecimalField(db_column='Sum_depoL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_depos = models.DecimalField(db_column='Sum_depoS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shift_num = models.CharField(db_column='Shift_num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    online_id = models.CharField(db_column='Online_Id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    wrist_num = models.CharField(db_column='Wrist_num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kass_doc_rec = models.DateTimeField(db_column='Kass_Doc_Rec', blank=True, null=True)  # Field name made lowercase.
    s_refund = models.DecimalField(db_column='S_Refund', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    s_foc = models.DecimalField(db_column='S_FOC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    card_num = models.CharField(db_column='Card_num', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    canceled = models.BooleanField(db_column='Canceled', blank=True, null=True)  # Field name made lowercase.
    recieptprinted = models.BooleanField(db_column='RecieptPrinted', blank=True, null=True)  # Field name made lowercase.
    wristbandprinted = models.BooleanField(db_column='WristbandPrinted', blank=True, null=True)  # Field name made lowercase.
    taxiid = models.CharField(db_column='TaxiID', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    taxireward = models.DecimalField(db_column='TaxiReward', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxirewardsticker = models.DecimalField(db_column='TaxiRewardSticker', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canceled_date = models.DateTimeField(db_column='Canceled_Date', blank=True, null=True)  # Field name made lowercase.
    canceled_empid = models.CharField(db_column='Canceled_EmpId', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agentreward = models.DecimalField(db_column='AgentReward', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pagernum = models.IntegerField(db_column='PagerNum', blank=True, null=True)  # Field name made lowercase.
    summcoupon = models.DecimalField(db_column='SummCoupon', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    testmode = models.CharField(db_column='TestMode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summ_cash1 = models.DecimalField(db_column='Summ_Cash1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_cash2 = models.DecimalField(db_column='Summ_Cash2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_change1 = models.DecimalField(db_column='Summ_Change1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_change2 = models.DecimalField(db_column='Summ_Change2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_tot2 = models.DecimalField(db_column='Summ_TOT2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    supervisorid = models.CharField(db_column='SupervisorID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sum_depoc = models.DecimalField(db_column='Sum_DepoC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kass_Doc'


class KassOper(models.Model):
    kass_oper_id = models.CharField(db_column='Kass_oper_id', primary_key=True, max_length=36)  # Field name made lowercase.
    order_in_doc = models.CharField(db_column='Order_in_Doc', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name_item = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    count_item = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    disc_item = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disc_chk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    summoncheck = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tip_oper = models.CharField(max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    vat = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)
    discnt_key = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    this_dscnt = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    proc_dscnt = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    is_vat = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    creat_time = models.DateTimeField(blank=True, null=True)
    rec_time = models.DateTimeField(blank=True, null=True)
    parentdoc_guid = models.CharField(db_column='Parentdoc_guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    parentdoc_num = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    foc_sign = models.SmallIntegerField(db_column='FOC_SIGN', blank=True, null=True)  # Field name made lowercase.
    nrecdoc = models.CharField(db_column='NRecDoc', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    order_pack = models.CharField(db_column='Order_pack', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_packet = models.CharField(db_column='Id_packet', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guidpacket = models.CharField(db_column='GuidPacket', max_length=36, blank=True, null=True)  # Field name made lowercase.
    taxireward = models.DecimalField(db_column='TaxiReward', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxirewardsticker = models.DecimalField(db_column='TaxiRewardSticker', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    printcoupon = models.BooleanField(db_column='PrintCoupon', blank=True, null=True)  # Field name made lowercase.
    printbyeachitem = models.BooleanField(db_column='PrintByEachItem', blank=True, null=True)  # Field name made lowercase.
    packetsdetailid = models.CharField(db_column='PacketsDetailId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    agentreward = models.DecimalField(db_column='AgentReward', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dsc_card_number = models.CharField(db_column='DSC_CARD_NUMBER', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_card_id = models.CharField(db_column='DSC_CARD_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    bonusup = models.DecimalField(db_column='BonusUp', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonuspay = models.DecimalField(db_column='BonusPay', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodsid = models.CharField(db_column='GoodsID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    couponsumm = models.DecimalField(db_column='CouponSumm', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    couponnum = models.CharField(db_column='CouponNum', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kass_oper'


class LastNom(models.Model):
    rowguid = models.CharField(primary_key=True, max_length=36)
    doc_id = models.CharField(db_column='Doc_id', unique=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    last_nom = models.IntegerField(db_column='Last_nom')  # Field name made lowercase.
    func = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LAST_NOM'


class Localuserright(models.Model):
    listright = models.CharField(db_column='ListRight', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocalUserRight'


class Localusers(models.Model):
    userid = models.CharField(db_column='UserID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userscancod = models.CharField(db_column='UserScanCod', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    listright = models.CharField(db_column='ListRight', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pin = models.IntegerField(db_column='Pin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocalUsers'


class Lockercontrollers(models.Model):
    controllernum = models.IntegerField(db_column='ControllerNum', blank=True, null=True)  # Field name made lowercase.
    roomnumber = models.IntegerField(db_column='RoomNumber', blank=True, null=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maxnumlockers = models.IntegerField(db_column='MaxNumLockers', blank=True, null=True)  # Field name made lowercase.
    xleft = models.IntegerField(db_column='xLeft', blank=True, null=True)  # Field name made lowercase.
    ytop = models.IntegerField(db_column='yTop', blank=True, null=True)  # Field name made lowercase.
    xwidth = models.IntegerField(db_column='xWidth', blank=True, null=True)  # Field name made lowercase.
    yheight = models.IntegerField(db_column='yHeight', blank=True, null=True)  # Field name made lowercase.
    lockernumbers = models.CharField(db_column='LockerNumbers', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    minnumber = models.CharField(db_column='MinNumber', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maxnumber = models.CharField(db_column='MaxNumber', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordertype = models.CharField(db_column='OrderType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LockerControllers'


class Lockers(models.Model):
    lockerid = models.CharField(db_column='LockerId', primary_key=True, max_length=36)  # Field name made lowercase.
    outnumber = models.IntegerField(db_column='OutNumber', blank=True, null=True)  # Field name made lowercase.
    controllernum = models.IntegerField(db_column='ControllerNum', blank=True, null=True)  # Field name made lowercase.
    phisnumberoflocker = models.IntegerField(db_column='PhisNumberOfLocker', blank=True, null=True)  # Field name made lowercase.
    roomnumber = models.IntegerField(db_column='RoomNumber', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wristbandid = models.CharField(db_column='WristbandID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    timelock = models.DateTimeField(db_column='TimeLock', blank=True, null=True)  # Field name made lowercase.
    recieptid = models.CharField(db_column='RecieptId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lockers'


class Luckytimeskdk(models.Model):
    luckytimeid = models.CharField(db_column='LuckyTimeId', primary_key=True, max_length=36)  # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.
    dsc_scheme_code = models.CharField(db_column='DSC_SCHEME_CODE', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cod_skdk = models.CharField(db_column='Cod_SKDK', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    discount_proc = models.DecimalField(db_column='Discount_Proc', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LuckyTimeSkdk'


class Onlinedocoper(models.Model):
    onlinedocoperid = models.CharField(db_column='OnlineDocOperId', primary_key=True, max_length=36)  # Field name made lowercase.
    onlinedocid = models.CharField(db_column='OnlineDocId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    onlineoper = models.CharField(db_column='OnlineOper', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    order_in_doc = models.CharField(db_column='Order_in_doc', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name_item = models.CharField(db_column='Name_item', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price_item = models.DecimalField(db_column='Price_Item', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    count_item = models.IntegerField(db_column='Count_item', blank=True, null=True)  # Field name made lowercase.
    guidpacket = models.CharField(db_column='GuidPacket', max_length=36, blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='Rectime', blank=True, null=True)  # Field name made lowercase.
    packetscod = models.CharField(db_column='PacketsCod', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnLineDocOper'
        unique_together = (('onlinedocid', 'packetscod'),)


class Onlinedoc(models.Model):
    onlinedocid = models.CharField(db_column='OnLineDocId', primary_key=True, max_length=36)  # Field name made lowercase.
    onlinenum = models.CharField(db_column='OnLineNum', unique=True, max_length=13, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    onlinedatesale = models.DateTimeField(db_column='OnlineDateSale', blank=True, null=True)  # Field name made lowercase.
    onlinecatalogid = models.CharField(db_column='OnlineCatalogId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    onlinedocsum = models.DecimalField(db_column='OnLineDocSum', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    onlinedocstatus = models.CharField(db_column='OnlineDocStatus', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bankresponse = models.CharField(db_column='BankResponse', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEMAIL', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    useraddress = models.CharField(db_column='UserAddress', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kass_doc_date = models.DateTimeField(db_column='Kass_doc_Date', blank=True, null=True)  # Field name made lowercase.
    kass_doc_num = models.CharField(db_column='Kass_Doc_Num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agentcode = models.CharField(db_column='AgentCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ga_id = models.CharField(db_column='GA_ID', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OnlineDoc'


class Orgdeposite(models.Model):
    orgdepoid = models.CharField(db_column='OrgDepoId', primary_key=True, max_length=36)  # Field name made lowercase.
    orgid = models.CharField(db_column='OrgId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    operationdate = models.DateTimeField(db_column='OperationDate', blank=True, null=True)  # Field name made lowercase.
    operationsign = models.IntegerField(db_column='OperationSign', blank=True, null=True)  # Field name made lowercase.
    operationsumm = models.DecimalField(db_column='OperationSumm', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operationtype = models.CharField(db_column='OperationType', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reldocumentnum = models.CharField(db_column='RelDocumentNum', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationdesc = models.CharField(db_column='OperationDesc', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationcomment = models.CharField(db_column='OperationComment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationaccepted = models.BooleanField(db_column='OperationAccepted', blank=True, null=True)  # Field name made lowercase.
    usercreator = models.CharField(db_column='UserCreator', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datecreate = models.DateTimeField(db_column='DateCreate', blank=True, null=True)  # Field name made lowercase.
    usereditor = models.CharField(db_column='UserEditor', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dateedit = models.DateTimeField(db_column='DateEdit', blank=True, null=True)  # Field name made lowercase.
    deposittype = models.CharField(db_column='DepositType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dateuntil = models.DateTimeField(db_column='DateUntil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrgDeposite'


class Organization(models.Model):
    organizationid = models.CharField(db_column='OrganizationID', max_length=36)  # Field name made lowercase.
    oldcode = models.CharField(db_column='OldCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_code = models.CharField(db_column='Org_Code', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_group = models.CharField(db_column='Org_Group', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='Org_Name', unique=True, max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_address = models.CharField(db_column='Org_Address', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_phone1 = models.CharField(db_column='Org_Phone1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_fax = models.CharField(db_column='Org_Fax', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_contact = models.CharField(db_column='Org_Contact', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_mail = models.CharField(db_column='Org_Mail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_web = models.CharField(db_column='Org_Web', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tax_id = models.CharField(db_column='Tax_id', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_postcode = models.CharField(db_column='Org_PostCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_city = models.CharField(db_column='Org_City', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_country = models.CharField(db_column='Org_Country', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    canoverdraft = models.BooleanField(db_column='CanOverdraft', blank=True, null=True)  # Field name made lowercase.
    depositein = models.DecimalField(db_column='DepositeIn', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    depositeuse = models.DecimalField(db_column='DepositeUse', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nowbalanse = models.DecimalField(db_column='NowBalanse', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maxoverdraft = models.DecimalField(db_column='MaxOverdraft', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    responseperson = models.CharField(db_column='ResponsePerson', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organization'


class Outlet(models.Model):
    outlet = models.CharField(db_column='Outlet', primary_key=True, max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    manageramountaccess = models.BooleanField(db_column='ManagerAmountAccess', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Outlet'


class PosName(models.Model):
    pos_id = models.CharField(db_column='POS_ID', unique=True, max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    place_name = models.CharField(db_column='PLACE_NAME', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notusedepo = models.BooleanField(db_column='NotUseDepo', blank=True, null=True)  # Field name made lowercase.
    testmode = models.BooleanField(db_column='TestMode', blank=True, null=True)  # Field name made lowercase.
    testmodechar = models.CharField(db_column='TestModeChar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POS_NAME'


class PosTestmode(models.Model):
    pos_testmodeid = models.CharField(db_column='POS_TESTMODEID', primary_key=True, max_length=36)  # Field name made lowercase.
    pos_id = models.CharField(db_column='POS_ID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type_mode = models.CharField(db_column='TYPE_MODE', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time_form = models.TimeField(db_column='Time_Form', blank=True, null=True)  # Field name made lowercase.
    time_to = models.TimeField(db_column='Time_to', blank=True, null=True)  # Field name made lowercase.
    max_n = models.IntegerField(db_column='Max_N', blank=True, null=True)  # Field name made lowercase.
    max_w = models.IntegerField(db_column='Max_W', blank=True, null=True)  # Field name made lowercase.
    now_n = models.IntegerField(db_column='Now_N', blank=True, null=True)  # Field name made lowercase.
    now_w = models.IntegerField(db_column='Now_W', blank=True, null=True)  # Field name made lowercase.
    max_s = models.DecimalField(db_column='Max_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    now_s = models.DecimalField(db_column='Now_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POS_TESTMODE'


class Packets2Cagtegory(models.Model):
    packets2category = models.CharField(db_column='Packets2Category', primary_key=True, max_length=36)  # Field name made lowercase.
    packetsid = models.CharField(db_column='PacketsId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ticketcategoryid = models.CharField(db_column='TicketCategoryId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Packets2Cagtegory'
        unique_together = (('packetsid', 'ticketcategoryid'),)


class Packetsdetail(models.Model):
    packetsdetailid = models.CharField(db_column='PacketsDetailId', primary_key=True, max_length=36)  # Field name made lowercase.
    packetsmainid = models.ForeignKey('Packetsmain', models.DO_NOTHING, db_column='PacketsMainId', blank=True, null=True)  # Field name made lowercase.
    packetspriceid = models.ForeignKey('Packetsprice', models.DO_NOTHING, db_column='PacketsPriceId', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcount = models.IntegerField(db_column='ItemCount', blank=True, null=True)  # Field name made lowercase.
    itemdiscount = models.DecimalField(db_column='ItemDiscount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isfoc = models.BooleanField(db_column='IsFoc', blank=True, null=True)  # Field name made lowercase.
    itemtotprice = models.DecimalField(db_column='ItemTotPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemtopup = models.DecimalField(db_column='ItemTopUp', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    printcoupon = models.BooleanField(db_column='PrintCoupon', blank=True, null=True)  # Field name made lowercase.
    printbyeachitem = models.BooleanField(db_column='PrintByEachItem', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itembonusup = models.DecimalField(db_column='ItemBonusUp', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    overcolor = models.CharField(db_column='OverColor', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PacketsDetail'


class Packetsgrouplist(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(unique=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PacketsGroupList'


class Packetsmain(models.Model):
    packetsid = models.CharField(db_column='PacketsID', primary_key=True, max_length=36)  # Field name made lowercase.
    packetscode = models.CharField(db_column='PacketsCode', unique=True, max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    packetsname = models.CharField(db_column='PacketsName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datefrom = models.DateTimeField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.DateTimeField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    packetsprice = models.DecimalField(db_column='PacketsPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    packetsrange = models.IntegerField(db_column='PacketsRange', blank=True, null=True)  # Field name made lowercase.
    taxirewardbase = models.DecimalField(db_column='TaxiRewardBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxirewardsticker = models.DecimalField(db_column='TaxiRewardSticker', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    agentreward = models.DecimalField(db_column='AgentReward', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    packetsgroup = models.CharField(db_column='PacketsGroup', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    supplicant = models.CharField(db_column='Supplicant', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodid = models.CharField(db_column='PeriodId', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PacketsMain'


class Packetsprice(models.Model):
    packetspriceid = models.CharField(db_column='PacketsPriceId', primary_key=True, max_length=36)  # Field name made lowercase.
    packetspricecod = models.CharField(db_column='PacketsPriceCod', unique=True, max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    packetspricename = models.CharField(db_column='PacketsPriceName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    packetspricebase = models.DecimalField(db_column='PacketsPriceBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pp_n_adult = models.IntegerField(db_column='PP_N_Adult', blank=True, null=True)  # Field name made lowercase.
    pp_n_child = models.IntegerField(db_column='PP_N_Child', blank=True, null=True)  # Field name made lowercase.
    pp_n_limited = models.IntegerField(db_column='PP_N_Limited', blank=True, null=True)  # Field name made lowercase.
    pp_discount = models.DecimalField(db_column='PP_Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pp_deposite = models.DecimalField(db_column='PP_Deposite', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pp_bonuses = models.DecimalField(db_column='PP_Bonuses', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orderinpacket = models.IntegerField(db_column='OrderInPacket', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wristcolor = models.CharField(db_column='WristColor', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PacketsPrice'


class Packetssectionlist(models.Model):
    section = models.CharField(db_column='Section', primary_key=True, max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PacketsSectionList'


class Packetstargetmarketlist(models.Model):
    id = models.CharField(max_length=36, blank=True, null=True)
    name = models.CharField(unique=True, max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PacketsTargetMarketList'


class Perioddate(models.Model):
    perioddateid = models.CharField(db_column='PeriodDateId', primary_key=True, max_length=36)  # Field name made lowercase.
    periodid = models.CharField(db_column='PeriodId', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodstart = models.DateTimeField(db_column='PeriodStart', blank=True, null=True)  # Field name made lowercase.
    periodend = models.DateTimeField(db_column='PeriodEnd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodDate'


class Periodname(models.Model):
    periodid = models.CharField(db_column='PeriodId', primary_key=True, max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    periodname = models.CharField(db_column='PeriodName', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodName'


class Protocol(models.Model):
    protocol_id = models.CharField(db_column='Protocol_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    type_record = models.CharField(db_column='Type_record', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cod_station = models.CharField(db_column='Cod_station', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_record = models.DateTimeField(db_column='Date_record', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Protocol'


class Sessions(models.Model):
    sessionid = models.CharField(db_column='SessionId', primary_key=True, max_length=88, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    expires = models.DateTimeField(db_column='Expires')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LockDate')  # Field name made lowercase.
    lockcookie = models.IntegerField(db_column='LockCookie')  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked')  # Field name made lowercase.
    sessionitem = models.BinaryField(db_column='SessionItem', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags')  # Field name made lowercase.
    timeout = models.IntegerField(db_column='Timeout')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessions'


class ShiftDoc(models.Model):
    shift_doc_id = models.CharField(db_column='Shift_Doc_id', primary_key=True, max_length=36)  # Field name made lowercase.
    shift_num = models.CharField(db_column='Shift_num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shiftstart = models.DateTimeField(db_column='ShiftStart', blank=True, null=True)  # Field name made lowercase.
    shiftend = models.DateTimeField(db_column='ShiftEnd', blank=True, null=True)  # Field name made lowercase.
    cashstart = models.DecimalField(db_column='CashStart', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cashend = models.DecimalField(db_column='CashEnd', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    shift_doc_type = models.CharField(db_column='Shift_Doc_Type', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shift_doc_num = models.CharField(db_column='Shift_Doc_num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shift_doc_rectime = models.DateTimeField(db_column='Shift_Doc_rectime', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shift_doc_time = models.DateTimeField(db_column='Shift_Doc_Time', blank=True, null=True)  # Field name made lowercase.
    floatmoney = models.DecimalField(db_column='FloatMoney', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shift_doc'


class Shifts(models.Model):
    shiftid = models.CharField(db_column='ShiftId', primary_key=True, max_length=36)  # Field name made lowercase.
    pos_id = models.CharField(db_column='POS_ID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    empid = models.CharField(db_column='EmpId', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shiftstart = models.DateTimeField(db_column='ShiftStart', blank=True, null=True)  # Field name made lowercase.
    shiftend = models.DateTimeField(db_column='ShiftEnd', blank=True, null=True)  # Field name made lowercase.
    shiftstatus = models.CharField(db_column='ShiftStatus', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cashstart = models.DecimalField(db_column='CashStart', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cashend = models.DecimalField(db_column='CashEnd', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    shift_num = models.CharField(db_column='Shift_num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    summ_doc_sale = models.DecimalField(db_column='Summ_Doc_sale', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_refund = models.DecimalField(db_column='Summ_refund', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_foc = models.DecimalField(db_column='Summ_foc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_cash_get = models.DecimalField(db_column='Sum_cash_get', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_change = models.DecimalField(db_column='Sum_Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_wdepo_up = models.DecimalField(db_column='Sum_WDepo_Up', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sum_wdepo_down = models.DecimalField(db_column='Sum_WDepo_Down', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_income = models.DecimalField(db_column='Summ_Income', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_outcome = models.DecimalField(db_column='Summ_Outcome', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_floatmoney = models.DecimalField(db_column='Summ_Floatmoney', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_by_cash = models.DecimalField(db_column='Summ_By_Cash', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_by_card = models.DecimalField(db_column='Summ_By_Card', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_by_deposite = models.DecimalField(db_column='Summ_By_Deposite', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    summ_change = models.DecimalField(db_column='Summ_Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    count_doc = models.IntegerField(db_column='Count_doc', blank=True, null=True)  # Field name made lowercase.
    n_adult = models.IntegerField(db_column='N_Adult', blank=True, null=True)  # Field name made lowercase.
    n_child = models.IntegerField(db_column='N_Child', blank=True, null=True)  # Field name made lowercase.
    n_infant = models.IntegerField(db_column='N_Infant', blank=True, null=True)  # Field name made lowercase.
    n_limited = models.IntegerField(db_column='N_Limited', blank=True, null=True)  # Field name made lowercase.
    summ_goods = models.DecimalField(db_column='Summ_Goods', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shifts'


class Supplier(models.Model):
    supplierid = models.CharField(db_column='SupplierID', primary_key=True, max_length=36)  # Field name made lowercase.
    org_code = models.CharField(db_column='Org_Code', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_group = models.CharField(db_column='Org_Group', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='Org_Name', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_address = models.CharField(db_column='Org_Address', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_phone1 = models.CharField(db_column='Org_Phone1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_fax = models.CharField(db_column='Org_Fax', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_contact = models.CharField(db_column='Org_Contact', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_mail = models.CharField(db_column='Org_Mail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_web = models.CharField(db_column='Org_Web', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tax_id = models.CharField(db_column='Tax_id', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_postcode = models.CharField(db_column='Org_PostCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_city = models.CharField(db_column='Org_City', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    org_country = models.CharField(db_column='Org_Country', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    canoverdraft = models.BooleanField(db_column='CanOverdraft', blank=True, null=True)  # Field name made lowercase.
    depositein = models.DecimalField(db_column='DepositeIn', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    depositeuse = models.DecimalField(db_column='DepositeUse', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nowbalanse = models.DecimalField(db_column='NowBalanse', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maxoverdraft = models.DecimalField(db_column='MaxOverdraft', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    share_of_proceeds = models.DecimalField(db_column='Share_of_proceeds', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    goods_groupchar = models.CharField(db_column='Goods_GroupChar', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nontestmode = models.BooleanField(db_column='NonTestMode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'


class Supplier2Outlet(models.Model):
    supplier2outletid = models.CharField(db_column='Supplier2OutletId', primary_key=True, max_length=36)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    partofrevenue = models.DecimalField(db_column='PartOfRevenue', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hide = models.BooleanField(db_column='Hide', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier2Outlet'
        unique_together = (('supplierid', 'outlet'),)


class Supplieruser(models.Model):
    supplieruserid = models.CharField(db_column='SupplierUserId', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    supplierid = models.CharField(db_column='SupplierId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierUser'


class Surveyanswer(models.Model):
    surveyanswerid = models.CharField(db_column='SurveyAnswerId', primary_key=True, max_length=36)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kass_docid = models.CharField(db_column='Kass_docId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SurveyAnswer'


class Surveystd(models.Model):
    surveystdid = models.CharField(db_column='SurveyStdId', primary_key=True, max_length=36)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='Answer', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    answerorder = models.IntegerField(db_column='AnswerOrder', blank=True, null=True)  # Field name made lowercase.
    answeris = models.BooleanField(db_column='AnswerIs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SurveyStd'


class Taxireward(models.Model):
    rewardid = models.CharField(db_column='RewardId', primary_key=True, max_length=36)  # Field name made lowercase.
    driver_guid = models.CharField(db_column='Driver_GUID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    kass_doc_id = models.CharField(db_column='Kass_doc_id', max_length=36, blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.CharField(db_column='Doc_Num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True)  # Field name made lowercase.
    tax_out = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    photo_action = models.BinaryField(db_column='Photo_action', blank=True, null=True)  # Field name made lowercase.
    taxirewardmainid = models.CharField(db_column='TaxiRewardMainId', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxiReward'


class Taxirewardmain(models.Model):
    taxirewardmainid = models.CharField(db_column='TaxiRewardMainId', primary_key=True, max_length=36)  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.CharField(db_column='Doc_Num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='RecTime', blank=True, null=True)  # Field name made lowercase.
    tax_out = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    photo_action = models.BinaryField(db_column='Photo_action', blank=True, null=True)  # Field name made lowercase.
    totalcommis = models.DecimalField(db_column='TotalCommis', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    driver_guid = models.CharField(db_column='Driver_GUID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxiRewardMain'


class Ticketcategory(models.Model):
    ticketcategoryid = models.CharField(db_column='TicketCategoryId', primary_key=True, max_length=36)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adultprice = models.DecimalField(db_column='AdultPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    childprice = models.DecimalField(db_column='ChildPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fam21price = models.DecimalField(db_column='Fam21Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fam22price = models.DecimalField(db_column='Fam22Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fam23price = models.DecimalField(db_column='Fam23Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    limitedprice = models.DecimalField(db_column='LimitedPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    typeprogram = models.CharField(db_column='TypeProgram', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categorycod = models.CharField(db_column='CategoryCod', unique=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoryorder = models.CharField(db_column='CategoryOrder', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hostlevel = models.CharField(db_column='HostLevel', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    havebranch = models.CharField(db_column='HaveBranch', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categorysubcod = models.CharField(db_column='CategorySubCod', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    parentcategory = models.CharField(db_column='ParentCategory', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    discount_adult = models.DecimalField(db_column='Discount_Adult', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount_child = models.DecimalField(db_column='Discount_Child', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount_f1 = models.DecimalField(db_column='Discount_F1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount_f2 = models.DecimalField(db_column='Discount_F2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount_f3 = models.DecimalField(db_column='Discount_F3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount_lim = models.DecimalField(db_column='Discount_Lim', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount_towel = models.DecimalField(db_column='Discount_Towel', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='Date_From', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='Date_to', blank=True, null=True)  # Field name made lowercase.
    starthour = models.TimeField(db_column='StartHour', blank=True, null=True)  # Field name made lowercase.
    endhour = models.TimeField(db_column='EndHour', blank=True, null=True)  # Field name made lowercase.
    towelrent = models.DecimalField(db_column='TowelRent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    toweldeposit = models.DecimalField(db_column='TowelDeposit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    foc_list = models.CharField(db_column='Foc_LIST', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    minilockerrent = models.DecimalField(db_column='MiniLockerRent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minilockerdeposit = models.DecimalField(db_column='MiniLockerDeposit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    swimsuitrent = models.DecimalField(db_column='SwimsuitRent', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    swimsuitdeposit = models.DecimalField(db_column='SwimsuitDeposit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adult_max = models.IntegerField(db_column='Adult_MAX', blank=True, null=True)  # Field name made lowercase.
    adult_min = models.IntegerField(db_column='Adult_min', blank=True, null=True)  # Field name made lowercase.
    child_max = models.IntegerField(db_column='Child_max', blank=True, null=True)  # Field name made lowercase.
    child_min = models.IntegerField(db_column='Child_min', blank=True, null=True)  # Field name made lowercase.
    cantaxireward = models.BooleanField(db_column='CanTaxiReward', blank=True, null=True)  # Field name made lowercase.
    cansurvey = models.BooleanField(db_column='CanSurvey', blank=True, null=True)  # Field name made lowercase.
    dsc_scheme_code = models.CharField(db_column='DSC_SCHEME_CODE', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    show4guest = models.BooleanField(db_column='Show4Guest', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketCategory'


class User2Outlet(models.Model):
    user2outletid = models.CharField(db_column='User2OutletId', primary_key=True, max_length=36)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    netusersid = models.CharField(db_column='NetUsersId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    inputaccept = models.BooleanField(db_column='InputAccept', blank=True, null=True)  # Field name made lowercase.
    returnaccept = models.BooleanField(db_column='ReturnAccept', blank=True, null=True)  # Field name made lowercase.
    inputread = models.BooleanField(db_column='InputRead', blank=True, null=True)  # Field name made lowercase.
    returnread = models.BooleanField(db_column='ReturnRead', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User2Outlet'


class Voucher(models.Model):
    voucherid = models.CharField(db_column='VoucherId', primary_key=True, max_length=36)  # Field name made lowercase.
    vouchernum = models.CharField(db_column='VoucherNum', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    voucherdatesale = models.DateTimeField(db_column='VoucherDateSale', blank=True, null=True)  # Field name made lowercase.
    vouchercatalogid = models.CharField(db_column='VoucherCatalogId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    vouchersum = models.DecimalField(db_column='VoucherSum', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    voucherstatus = models.CharField(db_column='VoucherStatus', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bankresponse = models.CharField(db_column='BankResponse', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEMAIL', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    useraddress = models.CharField(db_column='UserAddress', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userphone = models.CharField(db_column='UserPhone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    kass_doc_date = models.DateTimeField(db_column='Kass_doc_Date', blank=True, null=True)  # Field name made lowercase.
    kass_doc_num = models.CharField(db_column='Kass_Doc_Num', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agentcode = models.CharField(db_column='AgentCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ga_id = models.CharField(db_column='GA_ID', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dateenterfrom = models.DateTimeField(db_column='DateEnterFrom', blank=True, null=True)  # Field name made lowercase.
    dateenteruntil = models.DateTimeField(db_column='DateEnterUntil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Voucher'


class Voucheroper(models.Model):
    voucheroperid = models.CharField(db_column='VoucherOperId', primary_key=True, max_length=36)  # Field name made lowercase.
    voucherid = models.CharField(db_column='VoucherId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    voucheroper = models.CharField(db_column='VoucherOper', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    order_in_doc = models.CharField(db_column='Order_in_doc', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name_item = models.CharField(db_column='Name_item', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price_item = models.DecimalField(db_column='Price_Item', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    count_item = models.IntegerField(db_column='Count_item', blank=True, null=True)  # Field name made lowercase.
    guidpacket = models.CharField(db_column='GuidPacket', max_length=36, blank=True, null=True)  # Field name made lowercase.
    rectime = models.DateTimeField(db_column='Rectime', blank=True, null=True)  # Field name made lowercase.
    packetscod = models.CharField(db_column='PacketsCod', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VoucherOper'


class VoucherTemp(models.Model):
    id = models.CharField(max_length=36, blank=True, null=True)
    serial = models.CharField(max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Voucher_temp'


class Wristdeposite(models.Model):
    wristdepoid = models.CharField(db_column='WristDepoId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    wrist_num = models.CharField(db_column='Wrist_NUM', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.CharField(db_column='OperationType', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationsign = models.IntegerField(db_column='OperationSign', blank=True, null=True)  # Field name made lowercase.
    operationsumm = models.DecimalField(db_column='OperationSumm', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    reldocumentnum = models.CharField(db_column='RelDocumentNum', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationdate = models.DateTimeField(db_column='OperationDate', blank=True, null=True)  # Field name made lowercase.
    operationdesc = models.CharField(db_column='OperationDesc', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operationaccepted = models.BooleanField(db_column='OperationAccepted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WristDeposite'


class Wristevents(models.Model):
    wristeventid = models.CharField(db_column='WristEventId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    wrist_num = models.CharField(db_column='Wrist_NUM', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wristeventdate = models.DateTimeField(db_column='WristEventDate', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    placeid = models.CharField(db_column='PLaceId', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WristEvents'


class WristManagersdeposit(models.Model):
    wrist_num = models.CharField(db_column='Wrist_NUM', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wrist_ManagersDeposit'


class Wristbandcolor(models.Model):
    color = models.CharField(db_column='Color', primary_key=True, max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    usedtype = models.CharField(db_column='UsedType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cmyc = models.CharField(db_column='CMYC', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    semafor = models.CharField(db_column='Semafor', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    servicekey = models.BooleanField(db_column='ServiceKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WristbandColor'


class Wristbands(models.Model):
    wrist_num = models.CharField(db_column='Wrist_NUM', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    wrist_type = models.CharField(db_column='Wrist_Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guest_name = models.CharField(db_column='Guest_NAME', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    g_phone = models.CharField(db_column='G_Phone', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    g_mail = models.CharField(db_column='G_Mail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    towel_depo = models.DecimalField(db_column='Towel_Depo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    top_up = models.DecimalField(db_column='Top_Up', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_sale = models.DateTimeField(db_column='Date_Sale', blank=True, null=True)  # Field name made lowercase.
    last_print = models.DateTimeField(db_column='Last_print', blank=True, null=True)  # Field name made lowercase.
    parent_doc = models.CharField(db_column='Parent_Doc', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    blocked = models.CharField(db_column='Blocked', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_blocked = models.DateTimeField(db_column='Date_Blocked', blank=True, null=True)  # Field name made lowercase.
    cause_blocked = models.CharField(db_column='Cause_Blocked', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    towel_get = models.DecimalField(db_column='Towel_Get', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    towel_ret = models.DecimalField(db_column='Towel_Ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    towel_depo_ret = models.DecimalField(db_column='Towel_Depo_Ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    parentdoc_guid = models.CharField(db_column='Parentdoc_guid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    top_up_rest = models.DecimalField(db_column='Top_up_rest', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lockeroutnumber = models.IntegerField(db_column='LockerOutNumber', blank=True, null=True)  # Field name made lowercase.
    ticketcategoryid = models.CharField(db_column='TicketCategoryId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vip_status = models.CharField(db_column='VIP_Status', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date_insert = models.DateTimeField(db_column='Date_insert', blank=True, null=True)  # Field name made lowercase.
    minilocker_depo = models.DecimalField(db_column='MiniLocker_Depo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minilocker_get = models.DecimalField(db_column='MiniLocker_Get', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minilocker_ret = models.DecimalField(db_column='MiniLocker_Ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minilocker_depo_ret = models.DecimalField(db_column='MiniLocker_Depo_Ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    swimsuit_depo = models.DecimalField(db_column='Swimsuit_Depo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    swimsuit_get = models.DecimalField(db_column='Swimsuit_Get', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    swimsuit_ret = models.DecimalField(db_column='Swimsuit_Ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    swimsuit_depo_ret = models.DecimalField(db_column='Swimsuit_Depo_ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimumbalance2refund = models.DecimalField(db_column='MinimumBalance2Refund', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nrecdoc = models.CharField(db_column='NRecDoc', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    guesttype = models.CharField(db_column='GuestType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_card_id = models.CharField(db_column='DSC_CARD_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dsc_card_number = models.CharField(db_column='DSC_CARD_NUMBER', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dateenterfrom = models.DateTimeField(db_column='DateEnterFrom', blank=True, null=True)  # Field name made lowercase.
    dateenteruntil = models.DateTimeField(db_column='DateEnterUntil', blank=True, null=True)  # Field name made lowercase.
    unlimbufet = models.BooleanField(db_column='UnlimBufet', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    testmode = models.CharField(db_column='TestMode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.
    date_activated = models.DateTimeField(db_column='Date_Activated', blank=True, null=True)  # Field name made lowercase.
    cabana_depo = models.DecimalField(db_column='Cabana_Depo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cabana_depo_ret = models.DecimalField(db_column='Cabana_Depo_Ret', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wristbands'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Holdkey(models.Model):
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    col3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holdkey'


class Members(models.Model):
    memberid = models.CharField(db_column='MemberId', primary_key=True, max_length=36)  # Field name made lowercase.
    user_id = models.FloatField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    time_added = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    phone = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    thai = models.FloatField(blank=True, null=True)
    lang = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    catalog_code = models.CharField(db_column='Catalog_Code', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dsc_card_id = models.CharField(db_column='DSC_CARD_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dsc_card_number = models.CharField(db_column='DSC_CARD_NUMBER', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'members'


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180, db_collation='SQL_Latin1_General_CP1_CI_AS')
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration'


class Packets2Goods(models.Model):
    packets2goodsid = models.CharField(db_column='Packets2GoodsID', max_length=36)  # Field name made lowercase.
    packetspriceid = models.CharField(db_column='PacketsPriceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodsid = models.CharField(db_column='goodsID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packets2goods'


class User(models.Model):
    username = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    auth_key = models.CharField(max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password_hash = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password_reset_token = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.SmallIntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    verification_token = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class WristNum(models.Model):
    wrist_num = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    serial = models.IntegerField(db_column='Serial', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wrist_num'
