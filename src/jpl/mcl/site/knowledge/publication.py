# encoding: utf-8

u'''MCL — Publication'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema


class IPublication(IKnowledgeObject):
    u'''An publication participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this publication.'),
        required=True
    )
    year = schema.Int(
        title=_(u'Year'),
        description=_(u'The year this publication was published.'),
        required=False,
    )
    author = schema.List(
        title=_(u'Authors'),
        description=_(u'Authors who wrote this publication.'),
        required=False,
        value_type=schema.TextLine(
            title=_(u'Author'),
            description=_(u'Individual author associated with this publication.')
        )
    )
    pmid = schema.TextLine(
        title=_(u'Pubmed ID'),
        description=_(u'This publications pubmed ID.'),
        required=False,
    )
    journal = schema.TextLine(
        title=_(u'Journal'),
        description=_(u'The publications was published in this journal.'),
        required=False,
    )


IPublication.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Publication')
IPublication.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#year': ('year', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#author': ('author', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#pmid': ('pmid', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#journal': ('journal', False)
})
IPublication.setTaggedValue('fti', 'jpl.mcl.site.knowledge.publication')
