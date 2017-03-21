# encoding: utf-8

u'''MCL — Species'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject


class ISpecies(IKnowledgeObject):
    u'''An species is a basic way to categorize living organisms.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this species.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this species.'),
        required=False,
    )


ISpecies.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False)
})
ISpecies.setTaggedValue('fti', 'jpl.mcl.site.knowledge.species')
ISpecies.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Species')
