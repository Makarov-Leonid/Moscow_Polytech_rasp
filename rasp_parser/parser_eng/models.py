from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

# class rasp(models.Model):
#     version =
#     date =
#     time =
#     list_of_groups =

class group_rasp(models.Model):
    group_number = models.CharField(max_length=30)
    teacher = models.CharField(max_length=100, default='unknow')
    subject = models.CharField(max_length=100, default='unknow')
    # date_from =
    # date_to =
    auditories = models.CharField(max_length=10, default='unknow')


    class day_choises(models.TextChoices):
        MONDAY      = 'MON', _('Monday')
        TUESDAY     = 'tue', _('tuesday')
        WEDNESDAY   = 'WED', _('Wednesday')
        THURSDAY    = 'THI', _('Thursday')
        FRIDAY      = 'FRI', _('Friday')
        SATURDAY    = 'SAT', _('Saturday')
        SUNDAY      = 'SUN', _('Sunday')

    day = models.CharField(
        max_length=3,
        choices=day_choises.choices,
        default=day_choises.MONDAY,
    )

    class lesson_number_choices(models.TextChoices):
        FIRST_LESSON    =   'FIR', _('first lesson')
        SECOND_LESSON   =   'SEC', _('second lesson')
        THIRD_LESSON    =   'THI', _('thied lesson')
        FOURTH_LESSON   =   'FOU', _('fourth lesson')
        FIFTH_LESSON    =   'FIF', _('fifth lesson')
        SIXTH_LESSON    =   'SIX', _('sixth lesson')
        SEVENTH_LESSON  =   'SEV', _('seventh lesson')

    lesson = models.CharField(
        max_length=3,
        choices=lesson_number_choices.choices,
        default=lesson_number_choices.FIRST_LESSON,
    )
