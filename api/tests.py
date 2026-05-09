from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from core.definitions import GD, PD
from core.models import UserProfile, UserAccess, Group
from core.services import AuthService

User = get_user_model()


class AgentsApiTests(APITestCase):

    def setUp(self):
        # seed
        AuthService.sync_permissions()

        # user setup
        self.agent_user = User.objects.create_user(
            username="agent",
        )
        ua = UserAccess.objects.create()
        UserProfile.objects.create(
            user=self.agent_user,
            user_access=ua,
        )
        # assign to AGENT group
        AuthService.assign_user_to_group(user=self.agent_user, group=GD.agent)

        self.ap_user = User.objects.create_user(
            username="agency_principal",
        )
        ua2 = UserAccess.objects.create()
        UserProfile.objects.create(
            user=self.ap_user,
            user_access=ua2,
        )
        # assign to AP group
        AuthService.assign_user_to_group(user=self.ap_user, group=GD.agency_principal)

        self.url = reverse("list-agents")

    def test_list_agents_can_be_accessed_by_ap(self):
        self.client.force_authenticate(
            user=self.ap_user
        )
        response = self.client.get(
            reverse("list-agents")
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_list_agents_cant_be_accessed_by_agent(self):
        self.client.force_authenticate(
            user=self.agent_user
        )
        response = self.client.get(
            reverse("list-agents")
        )
        self.assertEqual(response.status_code, 403)
