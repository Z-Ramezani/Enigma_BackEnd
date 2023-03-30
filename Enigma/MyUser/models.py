from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models, IntegrityError

from rest_framework.exceptions import ValidationError


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(**kwargs)
        email = self.normalize_email(email)
        user.email = email
        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        u = self.create_user(email, password, **kwargs)
        u.is_admin = True
        u.is_active = True
        u.save(using=self._db)
        return u


class MyUser(AbstractBaseUser):

    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='user/profile/', blank=True)
    """
    phone_number = models.CharField(max_length=50, default='', blank=True)
    telegram_id = models.CharField(max_length=50, default='', blank=True)
    whatsapp_id = models.CharField(max_length=50, default='', blank=True)
    """
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    """
    groupID = models.ForeignKey(members, related_name='group_member', on_delete=models.CASCADE)

    """

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
