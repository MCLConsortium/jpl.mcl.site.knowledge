# encoding: utf-8

u'''MCL — Project'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema


class IProject(IKnowledgeObject):
    u'''An project participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this project.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this project.'),
        required=False,
    )
    abbreviatedName = schema.TextLine(
        title=_(u'Abbreviated Name'),
        description=_(u"Abbreviation name of this project."),
        required=False,
    )


IProject.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Project')
IProject.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#abbreviatedName': ('abbreviatedName', False)
})
IProject.setTaggedValue('fti', 'jpl.mcl.site.knowledge.project')