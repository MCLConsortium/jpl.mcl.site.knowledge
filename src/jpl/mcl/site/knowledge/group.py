# encoding: utf-8

u'''MCL — Working Group'''

from . import MESSAGE_FACTORY as _
from ._base import IKnowledgeObject
from person import IPerson
from plone.formwidget.contenttree import ObjPathSourceBinder
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
            source=ObjPathSourceBinder(object_provides=IPerson.__identifier__)
        )
    )


IGroup.setTaggedValue('typeURI', u'https://mcl.jpl.nasa.gov/rdf/types.rdf#Group')
IGroup.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'http://purl.org/dc/terms/description': ('description', False),
    u'http://xmlns.com/foaf/0.1/member': ('members', True)
})
IGroup.setTaggedValue('fti', 'jpl.mcl.site.knowledge.group')