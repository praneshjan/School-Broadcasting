"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'broadcast.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from staff import models

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    title = 'School sample broadcasting'
    template = 'registration/dashboard.html'
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        '''
        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Group: Administration & Applications'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Applications'),
                    column=1,
                    collapsible=False,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',),
                )
            ]
        ))'''

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Admin'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))