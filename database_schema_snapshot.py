# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
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
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ManagementsBus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    no_plate = models.CharField(max_length=150)
    seats = models.IntegerField()
    departure_city = models.CharField(max_length=150)
    departure_time = models.DateField()
    arrival_city = models.CharField(max_length=100, blank=True, null=True)
    depart_time = models.TimeField(blank=True, null=True)
    is_available = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managements_bus'


class ManagementsPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    paymentmethod = models.CharField(db_column='paymentMethod', max_length=100)  # Field name made lowercase.
    transactionid = models.CharField(db_column='transactionId', max_length=100)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    ticket = models.OneToOneField('ManagementsTicket', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'managements_payment'


class ManagementsRoute(models.Model):
    id = models.BigAutoField(primary_key=True)
    departure_city = models.CharField(max_length=150)
    arrival_city = models.CharField(max_length=100, blank=True, null=True)
    distance = models.FloatField()
    timetaken = models.DurationField(db_column='timeTaken')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'managements_route'


class ManagementsRouteBuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    route = models.ForeignKey(ManagementsRoute, models.DO_NOTHING)
    bus = models.ForeignKey(ManagementsBus, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'managements_route_buses'
        unique_together = (('route', 'bus'),)


class ManagementsSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    departtime = models.DateTimeField(db_column='departTime')  # Field name made lowercase.
    arrivaltime = models.DateTimeField(db_column='arrivalTime')  # Field name made lowercase.
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bus = models.ForeignKey(ManagementsBus, models.DO_NOTHING)
    route = models.ForeignKey(ManagementsRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'managements_schedule'


class ManagementsSeat(models.Model):
    id = models.BigAutoField(primary_key=True)
    seat_number = models.IntegerField(unique=True)
    booked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'managements_seat'


class ManagementsTesting(models.Model):
    id = models.BigAutoField(primary_key=True)
    departure_date = models.DateField()
    no_of_seats = models.IntegerField(db_column='No_of_seats')  # Field name made lowercase.
    license = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'managements_testing'


class ManagementsTicket(models.Model):
    id = models.BigAutoField(primary_key=True)
    seat_no = models.CharField(max_length=50)
    passenger_name = models.CharField(max_length=100)
    passengerage = models.IntegerField(db_column='passengerAge')  # Field name made lowercase.
    gender = models.CharField(max_length=100)
    schedule = models.ForeignKey(ManagementsSchedule, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    pay = models.IntegerField(blank=True, null=True)
    bus = models.ForeignKey(ManagementsBus, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managements_ticket'


class ManagementsUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(db_column='secondName', max_length=100)  # Field name made lowercase.
    email = models.CharField(max_length=200)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'managements_userprofile'


class ManagementsUserprofileBookingHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    userprofile = models.ForeignKey(ManagementsUserprofile, models.DO_NOTHING)
    ticket = models.ForeignKey(ManagementsTicket, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'managements_userprofile_booking_history'
        unique_together = (('userprofile', 'ticket'),)
