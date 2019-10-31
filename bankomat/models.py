from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Cart(models.Model):
    cart_number = models.CharField(_('Cart Number'), max_length=16,
                                   validators=[MinLengthValidator(16)])
    password = models.PositiveIntegerField(_('Password'), validators=[MaxValueValidator(9999), MinValueValidator(1000)])
    balance = models.DecimalField(_('Balance'), max_digits=6, decimal_places=2)
    full_name = models.CharField(_('Full name'), unique=True, max_length=40)
    cvv = models.PositiveIntegerField(_('Cvv'), unique=True,
                                      validators=[MaxValueValidator(999), MinValueValidator(100)])
    end_date = models.DateField(_('End Date'))

    def __str__(self):
        return self.full_name
