# encoding: utf-8

u'''MCL — ParticipatingSite'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from project import IProject
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
    project = RelationList(
        title=_(u'Projects'),
        description=_(u'Projects associated with this Participating Site.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Project'),
            description=_(u'A single project worked upon in this Participating Site.'),
            source=ObjPathSourceBinder(object_provides=IProject.__identifier__)
        )
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


IParticipatingSite.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#FundedSite')
IParticipatingSite.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#project': ('project', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#organ': ('organ', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#staff': ('staff', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#pi': ('pi', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#institution': ('institution', True)
})
IParticipatingSite.setTaggedValue('fti', 'jpl.mcl.site.knowledge.participatingsite')