from _ast import mod

from django.core.validators import RegexValidator
from django.db import models


class ContactUs(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    subject = models.CharField(max_length=50, verbose_name="موضوع")
    email = models.EmailField(verbose_name="ایمیل", null=True, blank=True)
    iran_phone_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="Phone number must be entered in the format: '09XXXXXXXXX'. Exactly 11 digits allowed."
    )
    phone = models.CharField(max_length=11, validators=[iran_phone_regex], verbose_name="شماره موبایل")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده یا نه")


class Meta:
    verbose_name = "تماس با ما"


def __str__(self):
    return f"{self.fullname} در  موضوع {self.subject} با شماره {self.phone} میخواهد تماس داشته باشد"
