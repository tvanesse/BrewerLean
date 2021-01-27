from django.db import models
from django.contrib.auth.models import User

class Facility(models.Model):
    class Meta:
        verbose_name='Facility'
        verbose_name_plural='Facilities'
    facility_name = models.CharField(max_length=100)

    def __str__(self):
        return self.facility_name

class Tank(models.Model):
    class Meta:
        verbose_name_plural='Tanks'
    class TankType(models.TextChoices):
        FERMENTER = 'FV', 'Fermenter'
        BRITE = 'BT', 'Brite'
        UNI = 'UT', 'Unitank'

    tank_type = models.CharField(max_length=2,
                                 choices=TankType.choices,
                                 default=TankType.FERMENTER)
    tank_name = models.CharField(max_length=15)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.tank_name

class Staff(models.Model):
    class Meta:
        verbose_name_plural = 'Staff'

    class StaffRole(models.TextChoices):
        HOTSIDE = 'HS', 'Hot Side'
        COLDSIDE = 'CS', 'Cold Side'
        WAREHOUSE = 'WS', 'Warehouse'

    name = models.CharField(max_length=75, null=True)
    role = models.CharField(max_length=2,
                            choices=StaffRole.choices,
                            default=StaffRole.HOTSIDE)
    last_modified_on = models.DateField(auto_now=True)
    last_modified_by = models.ForeignKey(User,
                                         null=True,
                                         on_delete=models.SET_NULL,
                                         default=1)

    def __str__(self):
        return self.name

