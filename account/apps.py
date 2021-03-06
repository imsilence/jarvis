#encoding: utf-8

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AccountConfig(AppConfig):
    name = 'account'

    verbose_name = _('account')
    verbose_name_plural = _('account')