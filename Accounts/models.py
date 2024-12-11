from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class AccountManager(BaseUserManager):
    def _create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError(_("The given phone must be set!"))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 'user')  # Default role as 'user'
        return self._create_user(phone, password=None, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')  # Set role to 'admin' for superuser

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    iran_phone_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="Phone number must be entered in the format: '09XXXXXXXXX'. Exactly 11 digits allowed."
    )

    phone = models.CharField(
        max_length=11,
        unique=True,
        validators=[iran_phone_regex],
        verbose_name='Phone Number'
    )
    fullname = models.CharField(max_length=150, verbose_name='FullName', null=True, blank=True)

    is_staff = models.BooleanField(default=False, verbose_name='Staff Status')
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted Status')
    date_joined = models.DateTimeField(auto_now=True)

    # Add role field here
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='User Role'
    )

    objects = AccountManager()

    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f"{self.fullname}|{self.phone}"


class Admin(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name='Username')
    password = models.CharField(max_length=128, verbose_name='Password')
    is_active = models.BooleanField(default=True, verbose_name='Active Status')

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = 'admins'

    def __str__(self):
        return self.username

    # def save(self, *args, **kwargs):
    #     if not self.pk or not check_password(self.password):  # Ensure password is hashed only once
    #         self.password = make_password(self.password)
    #     super(Admin, self).save(*args, **kwargs)
