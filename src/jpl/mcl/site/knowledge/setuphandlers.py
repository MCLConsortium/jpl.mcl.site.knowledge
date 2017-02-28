# encoding: utf-8

u'''JPL MCL Site Knowledge — setup handlers.'''

from ._utils import publish
from plone.dexterity.utils import createContentInContainer
from plone.registry.interfaces import IRegistry
from ZODB.DemoStorage import DemoStorage
from zope.component import getUtility
import socket, logging
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException
from plone.app.textfield.value import RichTextValue

_logger = logging.getLogger(__name__)


# There has to be a better way of doing this:
# MCL ID is currently 39 in KSDB
if socket.gethostname() == 'tumor.jpl.nasa.gov' or socket.gethostname().endswith('.local'):
    _logger.warn(u'Using development KSDB on edrn-dev.jpl.nasa.gov instead of production')
    _rdfBaseURL = u'https://edrn-dev.jpl.nasa.gov/ksdb/publishrdf/?rdftype='
    _rdfBaseURL = u'http://localhost:8000/ksdb/publishrdf/?filterby=program&filterval=39&rdftype='
else:
    _rdfBaseURL = u'https://mcl.jpl.nasa.gov/ksdb/publishrdf/?filterby=program&filterval=39&rdftype='


def createKnowledgeFolders(setupTool):
    if setupTool.readDataFile('jpl.mcl.site.knowledge.txt') is None: return
    portal = setupTool.getSite()
    # Don't bother if we're running in the test fixture
    if hasattr(portal._p_jar, 'db') and isinstance(portal._p_jar.db().storage, DemoStorage): return
    if 'resources' in portal.keys():
        portal.manage_delObjects('resources')
    knowledge = createContentInContainer(
        portal, 'Folder', title=u'Resources',
        description=u"Research resources and data."
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.protocolfolder', title=u'Protocols',
        description=u'MCL Consortium studies',
        url=_rdfBaseURL + u'protocol', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'Folder', title=u'Signatures',
        description=u'Molecularly screened signatures are …'
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.participatingsitefolder', title=u'Participating Sites',
        description=u'Groups formed inter or intra organizations to participate in a common goal.',
        url=_rdfBaseURL + u'fundedsite', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.publicationfolder', title=u'Publications',
        description=u'Articles and other material published by the MCL Consortium.',
        url=_rdfBaseURL + u'publication', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'Folder', title=u'Standards',
        description=u'Standards and policies developed for the MCL Consortium.'
    )
    createContentInContainer(
        knowledge, 'Folder', title=u'Informatics Tools',
        description=u'Informatics tools developed for the MCL Consortium.'
    )
    createContentInContainer(
        knowledge, 'Folder', title=u'Bookshelf',
        description=u'Miscellaneous MCL publications.'
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.institutionfolder', title=u'Institutions',
        description=u'Universities, hospitals, and other institutions working with the consortium.',
        url=_rdfBaseURL + u'institution', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.organfolder', title=u'Organs',
        description=u'Organs are collections of tissues joined in structural unit to serve a common function.',
        url=_rdfBaseURL + u'organ', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.personfolder', title=u'People',
        description=u'Individuals working with and comprising the consortium.',
        url=_rdfBaseURL + u'person', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.degreefolder', title=u'Degrees',
        description=u'Academic degrees are qualifications awarded on successful completion of courses of study.',
        url=_rdfBaseURL + u'degree', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.diseasefolder', title=u'Diseases',
        description=u'Diseases being studied in MCL.',
        url=_rdfBaseURL + u'disease', ingestEnabled=True
    )


    if 'working-groups' in portal.keys():
        portal.manage_delObjects('working-groups')

    createContentInContainer(
        portal, 'jpl.mcl.site.knowledge.groupfolder', title=u'Working Groups',
        description=u'Working groups formed to work on protocols and studies.',
        url=_rdfBaseURL + u'group', ingestEnabled=True
    )

    publish(knowledge)
    registry = getUtility(IRegistry)
    registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [
        u'resources/organs',
        u'resources/degrees',
        u'resources/publications',
        u'resources/people',
        u'resources/institutions',
        u'resources/participating-sites',
        u'resources/protocols',
        u'working-groups',
        u'resources/diseases'
    ]
