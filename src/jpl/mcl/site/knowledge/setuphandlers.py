# encoding: utf-8

u'''JPL MCL Site Knowledge — setup handlers.'''

from ._utils import publish
from plone.dexterity.utils import createContentInContainer
from plone.registry.interfaces import IRegistry
from ZODB.DemoStorage import DemoStorage
from zope.component import getUtility
import socket, logging

_logger = logging.getLogger(__name__)


# There has to be a better way of doing this:
if socket.gethostname() == 'tumor.jpl.nasa.gov' or socket.gethostname().endswith('.local'):
    _logger.warn(u'Using development KSDB on edrn-dev.jpl.nasa.gov instead of production')
    _rdfBaseURL = u'https://edrn-dev.jpl.nasa.gov/ksdb/publishrdf/?rdftype='
    #_rdfBaseURL = u'http://localhost:8000/ksdb/publishrdf/?rdftype='
else:
    _rdfBaseURL = u'https://mcl.jpl.nasa.gov/ksdb/publishrdf/?rdftype='


def createKnowledgeFolders(setupTool):
    if setupTool.readDataFile('jpl.mcl.site.knowledge.txt') is None: return
    portal = setupTool.getSite()
    # Don't bother if we're running in the test fixture
    if hasattr(portal._p_jar, 'db') and isinstance(portal._p_jar.db().storage, DemoStorage): return
    if 'knowledge' in portal.keys(): return
    knowledge = createContentInContainer(
        portal, 'Folder', title=u'Knowledge',
        description=u"MCL's Knowledge Environment"
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.organfolder', title=u'Organs',
        description=u'Organs are collections of tissues joined in structural unit to serve a common function.',
        url=_rdfBaseURL + u'organ', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.degreefolder', title=u'Degrees',
        description=u'Academic degrees are qualifications awarded on successful completion of courses of study.',
        url=_rdfBaseURL + u'degree', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.personfolder', title=u'People',
        description=u'Individuals working with and comprising the consortium.',
        url=_rdfBaseURL + u'person', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.institutionfolder', title=u'Institutions',
        description=u'Universities, hospitals, and other institutions working with the consortium.',
        url=_rdfBaseURL + u'institution', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.participatingsitefolder', title=u'Participating Sites',
        description=u'Groups formed inter or intra organizations to participate in a common goal.',
        url=_rdfBaseURL + u'fundedsite', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.projectfolder', title=u'Projects',
        description=u'Projects that are being worked on.',
        url=_rdfBaseURL + u'project', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.protocolfolder', title=u'Protocols',
        description=u'Protocols established in this consortium.',
        url=_rdfBaseURL + u'protocol', ingestEnabled=True
    )
    createContentInContainer(
        knowledge, 'jpl.mcl.site.knowledge.publicationfolder', title=u'Publications',
        description=u'Publications associated with this consortium.',
        url=_rdfBaseURL + u'publication', ingestEnabled=True
    )
    publish(knowledge)
    registry = getUtility(IRegistry)
    registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [
        u'knowledge/organs',
        u'knowledge/degrees',
        u'knowledge/people',
        u'knowledge/institutions',
        u'knowledge/participating-sites',
        u'knowledge/projects',
        u'knowledge/protocols',
        u'knowledge/publications'
    ]
