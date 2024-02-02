from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserInfo(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    student_user = models.BooleanField(default=False, verbose_name='وضعیت دانشجویی')

    def is_student(self):
        if self.is_superuser or self.is_staff:
            return False
        else:
            return True
    is_student.boolean = True
    is_student.short_description = 'وضعیت دانشجویی'