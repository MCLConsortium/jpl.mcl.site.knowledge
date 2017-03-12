# encoding: utf-8

u'''MCL — Person'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from ._utils import getReferencedBrains
from Acquisition import aq_inner
from degree import IDegree
from five import grok
from plone.app.vocabularies.catalog import CatalogSource
from plone.memoize import view
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema
import plone.api

FOAF_SURNAME = u'http://xmlns.com/foaf/0.1/surname'
FOAF_GIVENNAME = u'http://xmlns.com/foaf/0.1/givenname'


class IPerson(IKnowledgeObject):
    u'''An individual member of the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Full name of this person.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this person.'),
        required=False,
    )
    surname = schema.TextLine(
        title=_(u'Surname'),
        description=_(u'Surname (family name, last name, etc.) of this person.'),
        required=False,
    )
    givenName = schema.TextLine(
        title=_(u'Given Name'),
        description=_(u'Given name (first name, etc.) of this person.'),
        required=False,
    )
    degrees = RelationList(
        title=_(u'Degrees'),
        description=_(u'Academic degrees conferred upon this person.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Degree'),
            description=_(u'A single academic degree conferred upon this person.'),
            source=CatalogSource(object_provides=IDegree.__identifier__)
        )
    )
    email = schema.TextLine(
        title=_(u'Email Address'),
        description=_(u'Electronic mail address via which this person may be contacted.'),
        required=False,
    )
    phone = schema.TextLine(
        title=_(u'Telephone Number'),
        description=_(u'Public switched telephone network number where this person may be called.'),
        required=False,
    )
    dcbflag = schema.Bool(
        title=_(u'Part of DCB?'),
        description=_(u'True (checked) if person is part of DCB Committee'),
        required=False,
    )
    dcpflag = schema.Bool(
        title=_(u'Part of DCP?'),
        description=_(u'True (checked) if person is part of DCP Committee'),
        required=False,
    )

IPerson.setTaggedValue('predicateMap', {
    FOAF_SURNAME: ('surname', False),
    FOAF_GIVENNAME: ('givenName', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#degree': ('degrees', True),
    u'http://xmlns.com/foaf/0.1/mbox': ('email', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#has_dcp': ('dcpflag', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#has_dcb': ('dcbflag', False),
    u'http://xmlns.com/foaf/0.1/phone': ('phone', False)
})
IPerson.setTaggedValue('fti', 'jpl.mcl.site.knowledge.person')
IPerson.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Person')


class View(grok.View):
    u'''View for a Person'''
    grok.context(IPerson)
    grok.require('zope2.View')
    @view.memoize
    def degrees(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.degrees)
