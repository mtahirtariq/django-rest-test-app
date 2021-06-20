from django.db import models
from django.utils.translation import ugettext_lazy as _


class Customer(models.Model):
    """Model to store customers"""
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50, blank=False, null=False)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50, blank=False, null=False)
    dob = models.DateField(verbose_name=_('Date of Birth'), blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Policy(models.Model):
    """Model to store quotes/policies"""
    class State(models.TextChoices):
        NEW = ('new', _('New'))
        QUOTED = ('quoted', _('Quoted'))
        ACCEPTED = ('accepted', _('Accepted'))
        ACTIVE = ('active', _('Active'))

    customer = models.ForeignKey(
        to='core.Customer',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='policies',
    )
    type = models.CharField(max_length=50, blank=False, null=False)
    premium = models.IntegerField(blank=False, null=False)
    cover = models.IntegerField(blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False, choices=State.choices, default=State.NEW)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = _('Policies')

    def __str__(self):
        return f'{self.__class__.__name__}|{self.pk}|{self.state}|{self.customer}'
