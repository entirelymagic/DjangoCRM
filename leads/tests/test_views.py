from django.test import TestCase, Client
from django.shortcuts import reverse


class LandingPageTest(TestCase):

    # def decorator_get(self):
    #     response = self.client.get(reverse("landing_page"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "landing.html")
    #

    def _decorator_get(self):
        def wrapper(url, html_page):
            response = self.client.get(reverse(url))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, html_page)

        return wrapper

    @_decorator_get
    def test_get(self, url="landing_page", html_page="landing.html"):
        pass
