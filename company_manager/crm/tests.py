from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from crm.models import Company, Opportunity


class CRMViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("jirka", "jirka@mojefirma.cz", "tajne-heslo")
        Company.objects.create(name="THE MAMA AI", phone_number="123", identification_number="100000")
        self.user.user_permissions.add(Permission.objects.get(codename='add_opportunity'))

    def test_get_company_create(self):
        self.client.login(username="jirka", password="tajne-heslo")
        response = self.client.get(reverse("company_create"))
        self.assertEqual(response.status_code, 200)

    def test_post_company_create(self):
        self.client.login(username="jirka", password="tajne-heslo")
        response = self.client.post(reverse("company_create"),
                                    data={"name": "Test 2",
                                          "status": "N",
                                          "phone_number": "712 123456",
                                          "identification_number": "123456789"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Company.objects.count(), 2)

    def test_company_list_not_signed(self):
        response = self.client.get(reverse("company_list"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/company/list")

    def test_company_list(self):
        self.client.login(username="jirka", password="tajne-heslo")
        response = self.client.get(reverse("company_list"))
        self.assertContains(response, "THE MAMA AI")

    def test_post_opportunity_create(self):
        self.client.login(username="jirka", password="tajne-heslo")
        response = self.client.post(reverse("opportunity_create"),
                                    data={"company": "1",
                                          "sales_manager": "1",
                                          "status": "1"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Opportunity.objects.count(), 1)
