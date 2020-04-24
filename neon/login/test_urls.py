from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url =  reverse('loginIndex')
        self.assertEquals(resolve(url).func, index)
    
    def test_auth_url_is_resolved(self):
        url =  reverse('auth')
        self.assertEquals(resolve(url).func, auth_view)

    def test_loggedin_url_is_resolved(self):
        url =  reverse('loggedin')
        self.assertEquals(resolve(url).func, loggedin)

    def test_invalidlogin_url_is_resolved(self):
        url =  reverse('invalidlogin')
        self.assertEquals(resolve(url).func, invalidlogin)

    def test_logout_url_is_resolved(self):
        url =  reverse('logout')
        self.assertEquals(resolve(url).func, logout)
