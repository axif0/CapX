from django.test import TestCase, Client
from django.urls import reverse
from .models import Bug

class BugModelTestCase(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            bugTitle="Test Bug",
            bugDescription="This is a test bug description.",
            tag="Test Tag",
            subscribers="Test Subscribers",
            assign_to="Test Assign To"
        )

    def test_bug_creation(self):
        self.assertEqual(self.bug.bugTitle, "Test Bug")
        self.assertEqual(self.bug.bugDescription, "This is a test bug description.")
        self.assertEqual(self.bug.tag, "Test Tag")
        self.assertEqual(self.bug.subscribers, "Test Subscribers")
        self.assertEqual(self.bug.assign_to, "Test Assign To")

    def test_bug_str_representation(self):
        self.assertEqual(str(self.bug), "Test Bug")

class BugViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.bug = Bug.objects.create(
            bugTitle="Test Bug",
            bugDescription="This is a test bug description.",
            tag="Test Tag",
            subscribers="Test Subscribers",
            assign_to="Test Assign To"
        )

    def test_bug_list_view(self):
        response = self.client.get(reverse("succese"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")

    def test_bug_detail_view(self):
        response = self.client.get(reverse("update_bug", args=[self.bug.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")

    def test_bug_create_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

        # Check for 'Add a Bug' instead of 'Create Bug'
        self.assertContains(response, 'Add a Bug')

    def test_bug_update_view(self):
        response = self.client.get(reverse("update_bug", args=[self.bug.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Bug")

    def test_bug_delete_view(self):
        response = self.client.get(reverse("delete_bug", args=[self.bug.pk]))
        self.assertEqual(response.status_code, 302)  # Check for a successful redirect

# -----------------------------------------------------------------------------
    def test_bug_update_form_submission(self):
        response = self.client.post(reverse("update_bug", args=[self.bug.pk]), {
            "bugTitle": "Updated Test Bug",
            "bugDescription": "This is an updated test bug description.",
            "tag": "Updated Test Tag",
            "subscribers": "Updated Test Subscribers",
            "assign_to": "Updated Test Assign To",
        })
        self.assertEqual(response.status_code, 302)  # Check for a successful redirect
        self.assertRedirects(response, '/suc-cese/')  # Update to the expected redirect URL
