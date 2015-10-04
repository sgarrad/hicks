# -*- coding: utf-8 -*-

from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class HicksAccountAdapter(DefaultAccountAdapter):
    """Custom implementation of DefaultAccountAdapter from allauth to change
    the ability to disable signups
    """

    def is_open_for_signup(self, request):
        """Checks whether or not the site is open for signups.

        Setting `HICKS_SIGNUPS_ENABLED = False` in config.settings.common will
        override the default True setting.
        """
        return getattr(settings, 'HICKS_SIGNUPS_ENABLED', True)
