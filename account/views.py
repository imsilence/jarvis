#encoding: utf-8

from django.utils.translation import gettext as _
from django.http import HttpResponse

def index(request):
    return HttpResponse(_("account"))