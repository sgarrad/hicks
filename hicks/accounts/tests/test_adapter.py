# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.utils import override_settings
from django.test.client import RequestFactory

from ..adapter import HicksAccountAdapter


class TestHicksAccountAdapter(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @override_settings(
        HICKS_SIGNUPS_ENABLED=True
    )
    def test_is_open_for_signup_allowed(self):
        request = self.factory.get('/accounts/signup')
        hicks_account_adapter = HicksAccountAdapter()
        self.assertTrue(hicks_account_adapter.is_open_for_signup(request))

    @override_settings(
        HICKS_SIGNUPS_ENABLED=False
    )
    def test_is_open_for_signup_disallowed(self):
        request = self.factory.get('/accounts/signup')
        hicks_account_adpater = HicksAccountAdapter()
        self.assertFalse(hicks_account_adpater.is_open_for_signup(request))
