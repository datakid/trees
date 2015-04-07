from django.db import models

import .choices

class Tree(models.Model):
    genus = models.CharField(max_length=30, choices=GENUS_CHOICES)
    species = models.CharField(max_length=30, choices=SPECIES_CHOICES)
    dbh = models.IntegerField('Diameter at breast height, cm')
    ule_min = models.IntegerField('Lower bound on age, years')
    ule_max = models.IntegerField('Upper bound on age, years')

    crown = models.IntegerField('Width in metres of foliage', blank=True)
    height = models.IntegerField(blank=True, null=True)
    common = models.CharField(max_length=50, choices=COMMON_NAME_CHOICES, blank=True)
    location = models.CharField(max_length=4, choices=LOCATION_CHOICES, blank=True)
    ref = models.CharField(max_length=30, blank=True)
    maintenance_schedule = models.IntegerField(blank=True, null=True)
    last_maintenance = models.DateField(blank=True, null=True)
    maturity = models.CharField(length=1, choices=MATURITY_CHOICES, blank=True)
    planted = models.DateField(blank=True, null=True)
    captured = models.DateField(blank=True, null=True)
    health = models.CharField(max_length=1, choices=HEALTH_CHOICES, blank=True)
    structure = models.CharField(max_length=1, choices=STRUCTURE_CHOICES, blank=True)
