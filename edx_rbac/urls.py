# -*- coding: utf-8 -*-
"""
URLs for edx_rbac.
"""

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'', TemplateView.as_view(template_name="edx_rbac/base.html")),
]
