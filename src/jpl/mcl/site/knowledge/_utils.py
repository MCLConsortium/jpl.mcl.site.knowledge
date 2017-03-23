# encoding: utf-8

u'''MCL Site Knowledge — Utilities.'''


from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.WorkflowCore import WorkflowException
import plone.api


def publish(context, wfTool=None):
    u'''Publish the ``context`` item and all of its contents using the given
    ``wfTool``.  If no ``wfTool`` is given, we'll look up the portal_workflow
    tool.'''
    try:
        if wfTool is None: wfTool = plone.api.portal.get_tool('portal_workflow')
        wfTool.doActionFor(context, action='publish')
        context.reindexObject()
    except WorkflowException:
        pass
    if IFolderish.providedBy(context):
        for itemID, subItem in context.contentItems():
            publish(subItem, wfTool)


def getReferencedBrains(relations):
    u'''Given a ``relations`` sequence of RelationValue objects, return a sorted sequence
    of matching catalog brains for thoes objects.
    '''
    catalog = plone.api.portal.get_tool('portal_catalog')
    results = []
    for rel in relations:
        if rel.isBroken(): continue
        brains = catalog(path={'query': rel.to_path, 'depth': 0})
        results.append(brains[0])
    results.sort(lambda a, b: cmp(a['Title'].decode('utf-8'), b['Title'].decode('utf-8')))
    return results


class IngestResults(object):
    def __init__(self, created, updated, deleted):
        self.created, self.updated, self.deleted = created, updated, deleted
