# encoding: utf-8

u'''MCL — Protocol'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from ._utils import getReferencedBrains
from Acquisition import aq_inner
from five import grok
from organ import IOrgan
from participatingsite import IParticipatingSite
from person import IPerson
from plone.app.vocabularies.catalog import CatalogSource
from plone.memoize import view
from publication import IPublication
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema
import plone.api


class IProtocol(IKnowledgeObject):
    u'''An protocol participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this protocol.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Abstract'),
        description=_(u'A brief summary of this protocol.'),
        required=False,
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
            source=CatalogSource(object_provides=IPerson.__identifier__)
        )
    )
    custodian = RelationList(
        title=_(u'Custodians'),
        description=_(u'The custodian who provided to this protocol.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Custodian'),
            description=_(u'One of the custodians who provided this protocol.'),
            source=CatalogSource(object_provides=IPerson.__identifier__)
        )
    )
    organ = RelationList(
        title=_(u'Organs'),
        description=_(u'Organs associated with this protocol.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Organ'),
            description=_(u'A single organ studied in this protocol.'),
            source=CatalogSource(object_provides=IOrgan.__identifier__)
        )
    )
    publication = RelationList(
        title=_(u'Publications'),
        description=_(u'Publications associated with this Protocol.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Publication'),
            description=_(u'A single publication studied in this Protocol.'),
            source=CatalogSource(object_provides=IPublication.__identifier__)
        )
    )
    site = RelationList(
        title=_(u'Participating Sites'),
        description=_(u'Participating sites associated with this Protocol.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Participating Site'),
            description=_(u'A single participating site studied in this Protocol.'),
            source=CatalogSource(object_provides=IParticipatingSite.__identifier__)
        )
    )
    startDate = schema.Datetime(
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


IProtocol.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Protocol')
IProtocol.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/abstract': ('description', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#humanSubjectTraining': ('humanSubjectTraining', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#sitecontact': ('sitecontact', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#irbcontact': ('irbcontact', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#startDate': ('startDate', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#irbapprovalnum': ('irbapprovalnum', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#irbapproval': ('irbapproval', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#organ': ('organ', True),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#pi': ('pi', True),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#custodian': ('custodian', True),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#publication': ('publication', True),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#site': ('site', True)
})
IProtocol.setTaggedValue('fti', 'jpl.mcl.site.knowledge.protocol')


class View(grok.View):
    u'''View for a protocol'''
    grok.context(IProtocol)
    grok.require('zope2.View')
    @view.memoize
    def pis(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.pi)
    @view.memoize
    def custodians(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.custodian)
    @view.memoize
    def organs(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.organ)
    @view.memoize
    def publications(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.publication)
    @view.memoize
    def sites(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.site)
