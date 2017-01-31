# encoding: utf-8

u'''MCL — Protocol'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from organ import IOrgan
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema


class IProtocol(IKnowledgeObject):
    u'''An protocol participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this protocol.'),
        required=True
    )
    humanSubjectTraining = schema.Text(
        title=_(u'Human Subject Training'),
        description=_(u'Human subject training flag for this protocol.'),
        required=False,
    )
    sitecontact = schema.TextLine(
        title=_(u'Site Contact'),
        description=_(u'The site contact for this protocol.'),
        required=False,
    )
    irbcontact = schema.TextLine(
        title=_(u'IRB Contact'),
        description=_(u'IRB Contact email for this protocol.'),
        required=False,
    )
    pi = RelationList(
        title=_(u'PIs'),
        description=_(u'The principle investigator assigned to this protocol.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'PI'),
            description=_(u'A single PI assigned to this protocol.'),
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
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
    abstract = schema.TextLine(
        title=_(u'Abstract'),
        description=_(u'The abstract describing this protocol.'),
        required=False,
    )
    startDate = schema.TextLine(
        title=_(u'Start Date'),
        description=_(u'IRB Contact email for this protocol.'),
        required=False,
    )
    irbapprovalnum = schema.TextLine(
        title=_(u'IRB Approval Number'),
        description=_(u'IRB approval number used to approve this protocol.'),
        required=False,
    )
    irbapproval = schema.TextLine(
        title=_(u'IRB Approval'),
        description=_(u'Whether IRB Approved this protocol or not.'),
        required=False,
    )

IProtocol.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Protocol')
IProtocol.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/abstract': ('abstract', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#humanSubjectTraining': ('humanSubjectTraining', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#sitecontact': ('sitecontact', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#irbcontact': ('irbcontact', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#startDate': ('startDate', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#irbapprovalnum': ('irbapprovalnum', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#irbapproval': ('irbapproval', False),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#organ': ('organ', True),
    u'https://mcl.jpl.nasa.gov/rdf/schema.rdf#pi': ('pi', True)
})
IProtocol.setTaggedValue('fti', 'jpl.mcl.site.knowledge.protocol')