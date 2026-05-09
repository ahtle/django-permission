from django.db import transaction

from core.definitions import GD, PD, GroupDefinition, PermissionDefinition
from core.models import Group, Permission, UserAccess


class AuthService:

    @transaction.atomic
    def sync_permissions():
        """
        Keep Group and Permission in sync with values defined in GD and PD.
        This is called in post migration signal. If deploy script call migration,
        then we should always be in-sync.
        """

        declared_permission_keys = {definition.key for definition in PD.ALL}
        declared_group_keys = {definition.key for definition in GD.ALL}

        permission_map = {}

        for definition in PD.ALL:
            permission, _ = Permission.objects.update_or_create(
                key=definition.key,
                defaults={
                    "name": definition.name,
                    "description": definition.description,
                },
            )
            permission_map[definition.key] = permission

        # Remove stale groups first so their m2m links are cleaned before
        # deleting stale permissions.
        Group.objects.exclude(key__in=declared_group_keys).delete()

        for definition in GD.ALL:
            group, _ = Group.objects.update_or_create(
                key=definition.key,
                defaults={
                    "name": definition.name,
                },
            )
            permissions = [permission_map[p.key] for p in definition.permissions]
            group.permissions.set(permissions)

        # Delete permissions that no longer exist in PD.
        Permission.objects.exclude(key__in=declared_permission_keys).delete()

    @classmethod 
    def get_user_permissions(cls, user) -> set[str]:
        """ for a user, return set of permission keys """
        try: 
            access = user.profile.user_access 
        except UserAccess.DoesNotExist: 
            return set() 

        direct_permissions = set(
            access.permissions.values_list("key", flat=True)
        ) 
        group_permissions = set(
            access.groups.values_list("permissions__key", flat=True)
        ) 
        permissions = (direct_permissions | group_permissions)

        return permissions

    @classmethod 
    def user_has_any_permission(cls, user, permissions_list: list[PermissionDefinition]) -> bool: 

        user_permissions = cls.get_user_permissions(user) 
        return any(item.key in user_permissions for item in permissions_list)
    
    @staticmethod
    def assign_user_to_group(user, group: GroupDefinition):
        user_access = user.profile.user_access
        g = Group.objects.get(key=group.key)
        user_access.groups.add(g)
