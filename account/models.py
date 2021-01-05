#encoding: utf-8


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    username = models.CharField(
        verbose_name = _("account.user.username"),
        name = "username",
        max_length = 128,
        unique = True,
        blank = False,
        null = False,
        default = '',
        help_text = _("help.account.user.username"),
        validators = [UnicodeUsernameValidator()],
        error_messages = {
            'unique': _("error.account.user.username.unique"),
        },
    )

    nickname = models.CharField(
        verbose_name = _("account.user.nickname"),
        name = "nickname",
        max_length = 128,
        blank = False,
        null = False,
        default = '',
    )

    email = models.EmailField(
        verbose_name = _("account.user.email"),
        name = "email",
        blank = True,
        null = False,
        default = '',
    )

    telephone = models.CharField(
        verbose_name = _("account.user.telephone"),
        name = "telephone",
        max_length = 32,
        blank = True,
        null = False,
        default = '',
    )

    is_staff = models.BooleanField(
        verbose_name = _('account.user.is_staff'),
        name = 'is_staff',
        blank = False,
        null = False,
        default = False,
        help_text = _('help.account.user.is_staff'),
    )

    is_active = models.BooleanField(
        verbose_name = _('account.user.is_active'),
        name = 'is_active',
        blank = False,
        null = False,
        default = True,
        help_text = _('help.acount.user.is_active'),
    )

    created_at = models.DateTimeField(
        verbose_name = _("account.user.created_at"),
        name = "created_at",
        blank = False,
        null = False,
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        verbose_name = _("account.user.updated_at"),
        name = "updated_at",
        blank = False,
        null = False,
        auto_now = True,
    )

    deleted_at = models.DateTimeField(
        verbose_name = _("account.user.deleted_at"),
        name = "deleted_at",
        blank = True,
        null = True,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'email', 'telephone']

    class Meta:
        verbose_name = _('account.user')
        verbose_name_plural = _('account.users')