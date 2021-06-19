from django.db import models


class Customer(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=50, blank=False, null=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=50, blank=False, null=False)
    dob = models.DateField(verbose_name='Date of Birth', blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
