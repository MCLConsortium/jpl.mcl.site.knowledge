# encoding: utf-8

u'''MCL — Working Group'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from ._utils import getReferencedBrains
from Acquisition import aq_inner
from five import grok
from person import IPerson
from plone.app.textfield import RichText
from plone.app.vocabularies.catalog import CatalogSource
from plone.memoize import view
from z3c.relationfield.schema import RelationChoice, RelationList
from zope import schema


class IGroup(IKnowledgeObject):
    u'''A working group participating with the MCL consortium.'''
    title = schema.TextLine(
        title=_(u'Name'),
        description=_(u'Name of this working group.'),
        required=True
    )
    description = schema.Text(
        title=_(u'Description'),
        description=_(u'A short summary of this working group.'),
        required=False,
    )
    members = RelationList(
        title=_(u'Members'),
        description=_(u'People employed or consulting to this group.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Member'),
            description=_(u'A single member of this group.'),
            source=CatalogSource(object_provides=IPerson.__identifier__)
        )
    )
    chairs = RelationList(
        title=_(u'Chair(s)'),
        description=_(u'Chair(s) of this group.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Chair'),
            description=_(u'A single chair of this group.'),
            source=CatalogSource(object_provides=IPerson.__identifier__)
        )
    )
    cochairs = RelationList(
        title=_(u'Co-Chair(s)'),
        description=_(u'Co-chairs of this group.'),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_(u'Co-Chair'),
            description=_(u'A single co-chair of this group.'),
            source=CatalogSource(object_provides=IPerson.__identifier__)
        )
    )
    additionalText = RichText(title=u"Additional Text", 
        description=_(u'Any additional rich text information you want to add to this working group.'),
        required=False)


class View(grok.View):
    u'''View for a working group.'''
    grok.context(IGroup)
    grok.require('zope2.View')
    @view.memoize
    def chairs(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.chairs)
    @view.memoize
    def cochairs(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.cochairs)
    @view.memoize
    def members(self):
        context = aq_inner(self.context)
        return getReferencedBrains(context.members)


IGroup.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Group')
IGroup.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#chair': ('chairs', True),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#cochair': ('cochairs', True),
    u'http://xmlns.com/foaf/0.1/member': ('members', True)
})
IGroup.setTaggedValue('fti', 'jpl.mcl.site.knowledge.group')
