# encoding: utf-8

u'''MCL — Institution'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema


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
        description=_(u'And abbreviated name or acronym to simplify identifying this institution.'),
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
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
        )
    )


IInstitution.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Institution')
IInstitution.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#department': ('department', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#abbreviatedName': ('abbreviation', False),
    u'http://xmlns.com/foaf/0.1/homepage': ('homepage', False),
    u'http://xmlns.com/foaf/0.1/member': ('members', True)
})
IInstitution.setTaggedValue('fti', 'jpl.mcl.site.knowledge.institution')