from django.db import models
from django.utils import timezone
from account.models import UserInfo
from django.urls import reverse

class Semester(models.Model):
    user = models.ForeignKey(UserInfo, default=None, on_delete=models.CASCADE, related_name='semesteruser',
                             verbose_name='کاربر')
    name = models.CharField(default=None, max_length=15, verbose_name='عنوان ترم')
    start_date = models.DateField(verbose_name='تاریخ شروع نیمسال')
    end_date = models.DateField(verbose_name='تاریخ پایان نیمسال')

    def is_even(self):
        days_pass = (timezone.now().date() - self.start_date).days
        week_number = int(days_pass / 7) + 1
        if week_number % 2 == 0:
            return False
        else:
            return True

    is_even.boolean = True
    is_even.short_description = 'هفته فرد'

    def get_absolute_url(self):
        return reverse('account:semester')

