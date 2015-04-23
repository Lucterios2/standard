# -*- coding: utf-8 -*-
'''
Created on 11 fevr. 2015

@author: sd-libre
'''

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _, ugettext
from os.path import join, dirname
import lucterios.standard

def get_subtitle():
    try:
        from django.apps.registry import apps
        legalentity = apps.get_model("contacts", "LegalEntity")
        our_detail = legalentity.objects.get(id=1)
        return our_detail.name
    except LookupError:
        return ugettext("Generic management application")

APPLIS_NAME = lucterios.standard.__title__()
APPLIS_VERSION = lucterios.standard.__version__
APPLI_EMAIL = "support@sd-libre.fr"
APPLIS_LOGO_NAME = join(dirname(__file__), "logo.gif")
APPLIS_COPYRIGHT = _("(c) GPL Licence")
APPLIS_SUBTITLE = get_subtitle
