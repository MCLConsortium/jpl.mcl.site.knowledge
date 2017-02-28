# encoding: utf-8

u'''MCL — ParticipatingSite'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from institution import IInstitution
from organ import IOrgan
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema


class IParticipatingSite(IKnowledgeObject):
    u'''An participatingsite participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this participating site.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this participating site.'),
        required=False,
    )
    organ = RelationList(
        title=_(u'Organs'),
        description=_(u'Organs associated with this Participating Site.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Organ'),
            description=_(u'A single organ studied in this Participating Site.'),
            source=ObjPathSourceBinder(object_provides=IOrgan.__identifier__)
        )
    )
    staff = RelationList(
        title=_(u'Staff'),
        description=_(u'Staff associated with this Participating Site.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Staff Member'),
            description=_(u'A individual staff member in this Participating Site.'),
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
        )
    )
    pi = RelationList(
        title=_(u'PIs'),
        description=_(u'PIs associated with this Participating Site.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'PI'),
            description=_(u'An individual PI in this Participating Site.'),
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
        )
    )
    contact = RelationList(
        title=_(u'Contacts'),
        description=_(u'Contacts in this Participating Site.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Contact'),
            description=_(u'An individual contact in this Participating Site.'),
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
        )
    )
    institution = RelationList(
        title=_(u'Institutions'),
        description=_(u'Institutions associated with this Participating Site.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Institution'),
            description=_(u'A single institution studied in this Participating Site.'),
            source=ObjPathSourceBinder(object_provides=IInstitution.__identifier__)
        )
    )
    fundingStartDate = schema.TextLine(
        title=_(u'Funding Start Date'),
        description=_(u'Funding start date for this participating site.'),
        required=False,
    )
    fundingFinishDate = schema.TextLine(
        title=_(u'Funding Finish Date'),
        description=_(u'Funding finish date for this participating site.'),
        required=False,
    )


IParticipatingSite.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#FundedSite')
IParticipatingSite.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#organ': ('organ', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#staff': ('staff', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#pi': ('pi', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#contact': ('contact', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#fundingStartDate': ('fundingStartDate', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#fundingFinishDate': ('fundingFinishDate', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#institution': ('institution', True)
})
IParticipatingSite.setTaggedValue('fti', 'jpl.mcl.site.knowledge.participatingsite')