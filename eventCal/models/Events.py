from django.db import models
from django.db.models import Q
from eventCal.models.Eventcal_Abstract import EventCalAbstract
from account.models import UserInfo
from django.urls import reverse
from .Semester import Semester

class SubjectManager(models.Manager):
    def daily_report(self):
        if Semester.is_even:
            return self.filter(Q(status='f') | Q(status='a'))
        else:
            return self.filter(Q(status='z') | Q(status='a'))

    def even_week_report(self):
        return self.filter(Q(status='f') | Q(status='a'))

    def odd_week_report(self):
        return self.filter(Q(status='z') | Q(status='a'))

class SubjectEvent(EventCalAbstract):
    WEEK_STATUS = (
        ('z', 'زوج'),
        ('f', 'فرد'),
        ('a', 'هرهفته'),
    )
    DAYS = (
        ('0', 'شنبه'),
        ('1', 'یکشنبه'),
        ('2', 'دوشنبه'),
        ('3', 'سه شنبه'),
        ('4', 'چهارشنبه'),
        ('5', 'پنج شنبه'),
    )

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='subjectEvent', verbose_name='کاربر')
    title = models.CharField(max_length=200, verbose_name='عنوان درس')
    start_time = models.TimeField(verbose_name='ساعت شروع درس')
    end_time = models.TimeField(verbose_name='ساعت پایان درس')
    day = models.CharField(default=None, max_length=1, choices=DAYS, verbose_name='روز کلاس')
    status = models.CharField(max_length=1, choices=WEEK_STATUS, verbose_name='هفته')

    class Meta:
        verbose_name = 'رویداد درسی'
        verbose_name_plural = 'رویدادهای درسی'

    def __str__(self):
        return f' درس {self.title} متعلق به {str(self.user)}'

    def get_absolute_url(self):
        return reverse("account:home")

    objects = SubjectManager()


class PersonalEvent(EventCalAbstract):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='personalEvent', verbose_name='کاربر')
    title = models.CharField(max_length=200, verbose_name='موضوع(نام) رویداد')
    date = models.DateField(verbose_name='تاریخ رویداد')
    start_time = models.TimeField(verbose_name='ساعت شروع رویداد')
    end_time = models.TimeField(verbose_name='ساعت پایان رویداد')

    class Meta:
        verbose_name = 'رویداد شخصی'
        verbose_name_plural = 'رویدادهای شخصی'

    def __str__(self):
        return f' رویداد {self.title} متعلق به {self.user}'

    def get_absolute_url(self):
        return reverse("account:allpersonal")