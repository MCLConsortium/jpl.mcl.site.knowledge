# encoding: utf-8

u'''MCL — SpecimenType'''

from . import MESSAGE_FACTORY as _
from zope import schema
from ._base import IKnowledgeObject


class ISpecimenType(IKnowledgeObject):
    u'''An specimentype is a branch of knowledge studied under.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this specimentype.'),
        required=True,
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A brief description of this specimentype.'),
        required=False,
    )


ISpecimenType.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False)
})
ISpecimenType.setTaggedValue('fti', 'jpl.mcl.site.knowledge.specimentype')
ISpecimenType.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#SpecimenType')
