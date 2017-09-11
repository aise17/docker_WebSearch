# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from proof.models import Engine, Client, FileQuery, FileResults
# Register your models here.

admin.site.register(Engine)
admin.site.register(Client)
admin.site.register(FileResults)
admin.site.register(FileQuery)