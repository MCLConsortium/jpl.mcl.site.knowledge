# encoding: utf-8

u'''MCL — custom upgrade steps.'''


from plone.app.ldap.engine.interfaces import ILDAPConfiguration
from plone.app.ldap.engine.schema import LDAPProperty
from plone.app.ldap.ploneldap.util import guaranteePluginExists
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import INavigationSchema
from Products.PluggableAuthService.interfaces.plugins import (
    IAuthenticationPlugin, IPropertiesPlugin, IUserAdderPlugin, IUserEnumerationPlugin, IRolesPlugin,
    IRoleEnumerationPlugin, IGroupsPlugin, IGroupEnumerationPlugin, ICredentialsResetPlugin
)
from Products.PlonePAS.interfaces.plugins import IUserManagement
from Products.PlonePAS.interfaces.group import IGroupManagement, IGroupIntrospection
from zope.component import getUtility
import plone.api, socket, logging, os
from ._utils import publish, hideTab, rename, move

_logger = logging.getLogger(__name__)

def nullUpgradeStep(context):
    u'''Null upgrade step does nothing for when no custom behavior is needed.'''
    pass

def movePublications(context):
    u'''Install jpl.mcl.site.knowledge.'''
    portal = _getPortal(context)
    if 'publications' in portal['resources'].keys():
        move(portal['resources']['publications'], portal)
