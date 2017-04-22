from datetime import datetime

from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default='')
    city = models.CharField(max_length=10, default='')
    state = models.CharField(max_length=10, default='')
    country = models.CharField(max_length=30, default='')
    reg_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username

    def was_reg_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.reg_date <= now

    was_reg_recently.admin_order_field = 'reg_date'
    was_reg_recently.boolean = True
    was_reg_recently.short_description = 'Registered recently?'


# create and save donor object, after saving user object
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Donor.objects.create(user=kwargs['instance'])


'''
signal trigger
Specifying sender limits the receiver
to just post_save signals sent for saves of that particular model.
'''
post_save.connect(create_profile, sender=User)


# use post_save to trigger tweepy later
