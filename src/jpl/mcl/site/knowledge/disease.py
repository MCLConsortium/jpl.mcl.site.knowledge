# encoding: utf-8

u'''MCL — Disease'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject


class IDisease(IKnowledgeObject):
    u'''An disease is a collection of tissues joined in a structural unit to serve a common function.'''
    title = schema.TextLine(
        title=_(u'ICD10 Name'),
        description=_(u'ICD10 name of this disease.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this disease.'),
        required=False,
    )


IDisease.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False)
})
IDisease.setTaggedValue('fti', 'jpl.mcl.site.knowledge.disease')
IDisease.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Disease')
