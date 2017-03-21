# encoding: utf-8

u'''MCL — Institution'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from ._utils import getReferencedBrains
from Acquisition import aq_inner
from five import grok
from person import IPerson
from plone.app.vocabularies.catalog import CatalogSource
from plone.memoize import view
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema
import plone.api


class IInstitution(IKnowledgeObject):
    u'''An institution participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this institution.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this institution.'),
        required=False,
    )
    department = schema.TextLine(
        title=_(u'Department'),
        description=_(u'The specific department participating with MCL.'),
        required=False,
    )
    abbreviation = schema.TextLine(
        title=_(u'Abbreviation'),
        description=_(u'An abbreviated name or acronym to simplify identifying this institution.'),
        required=False,
    )
    homepage = schema.TextLine(
        title=_(u'Home Page'),
        description=_(u"URL to the site's home page."),
        required=False,
    )
    members = RelationList(
        title=_(u'Members'),
        description=_(u'People employed or consulting to this institution.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Member'),
            description=_(u'A single member of this institution.'),
            source=CatalogSource(object_provides=IPerson.__identifier__)
        )
    )


IInstitution.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Institution')
IInstitution.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#department': ('department', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#abbreviatedName': ('abbreviation', False),
    u'http://xmlns.com/foaf/0.1/homepage': ('homepage', False),
    u'http://xmlns.com/foaf/0.1/member': ('members', True)
})
IInstitution.setTaggedValue('fti', 'jpl.mcl.site.knowledge.institution')


class View(grok.View):
    u'''View for an institution'''
    grok.context(IInstitution)
    grok.require('zope2.View')
    @view.memoize
    def members(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.members)
