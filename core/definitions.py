from dataclasses import dataclass
from typing import List


@dataclass(frozen=True) 
class PermissionDefinition: 
    key: str 
    name: str 
    description: str = ""


class PD: 
    can_view_contact = PermissionDefinition(
        key="can_view_contact", 
        name="Can View Contact",
        description="Permission to view contact"
    )
    can_edit_contact = PermissionDefinition(
        key="can_edit_contact", 
        name="Can Edit Contact",
        description="Permission to edit contact"
    )
    can_view_agent = PermissionDefinition(
        key="can_view_agent", 
        name="Can View Agent",
        description="Permission to view agent"
    )

    ALL = (
        can_view_contact,
        can_edit_contact,
        can_view_agent,
    )


@dataclass(frozen=True) 
class GroupDefinition: 
    key: str 
    name: str 
    permissions: List[PermissionDefinition]


class GD:
    admin = GroupDefinition(
        key="admin",
        name="Admin",
        permissions=[PD.can_view_contact, PD.can_edit_contact, PD.can_view_agent]
    )
    agent = GroupDefinition(
        key="agent",
        name="Agent",
        permissions=[PD.can_view_contact,PD.can_edit_contact]
    )
    agency_principal = GroupDefinition(
        key="agency_principal", 
        name="Agency Principal", 
        permissions=[PD.can_view_agent]
    )

    ALL = (
        admin,
        agent,
        agency_principal,
    )