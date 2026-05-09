from django.test import TestCase

from core.models import Group, Permission
from core.services import AuthService


class SyncPermissionsTests(TestCase):
    def test_sync_permissions_deletes_stale_permission(self):
        stale = Permission.objects.create(
            key="stale_permission",
            name="Stale Permission",
            description="to be removed",
        )

        AuthService.sync_permissions()

        self.assertFalse(Permission.objects.filter(pk=stale.pk).exists())

    def test_sync_permissions_deletes_stale_group(self):
        stale_group = Group.objects.create(
            key="stale_group",
            name="Stale Group",
        )

        AuthService.sync_permissions()

        self.assertFalse(Group.objects.filter(pk=stale_group.pk).exists())
