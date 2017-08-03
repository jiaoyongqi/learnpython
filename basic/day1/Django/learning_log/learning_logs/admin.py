# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from learning_logs.models import Topic,Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)