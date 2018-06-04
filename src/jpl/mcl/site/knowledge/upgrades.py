# encoding: utf-8

u'''MCL — custom upgrade steps.'''


from ._utils import move
import plone.api


def nullUpgradeStep(context):
    u'''Null upgrade step does nothing for when no custom behavior is needed.'''
    pass


def movePublications(context):
    u'''Install jpl.mcl.site.knowledge.'''
    portal = plone.api.portal.get()
    if 'publications' in portal['resources'].keys():
        move(portal['resources']['publications'], portal)
