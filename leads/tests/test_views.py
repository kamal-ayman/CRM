from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):
    
    def test_status_code(self):
        # TODO some sort os test
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        # TODO some sort os test
        response = self.client.get(reverse("landing-page"))
        self.assertTemplateUsed(response, "landing.html")