# encoding: utf-8

u'''MCL — Discipline'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject


class IDiscipline(IKnowledgeObject):
    u'''An discipline is a branch of knowledge studied under.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this discipline.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this discipline.'),
        required=False,
    )


IDiscipline.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False)
})
IDiscipline.setTaggedValue('fti', 'jpl.mcl.site.knowledge.discipline')
IDiscipline.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Discipline')
