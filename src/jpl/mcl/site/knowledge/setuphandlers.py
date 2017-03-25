# encoding: utf-8

u'''JPL MCL Site Knowledge — setup handlers.'''

from ._utils import publish, hideTab, rename, move
from plone.dexterity.utils import createContentInContainer
from plone.registry.interfaces import IRegistry
from ZODB.DemoStorage import DemoStorage
from zope.component import getUtility
import socket, logging
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException
from plone.app.textfield.value import RichTextValue
#from Products.CMFPlone.interfaces import INavigationSchema

_logger = logging.getLogger(__name__)


# There has to be a better way of doing this:
# MCL ID is currently 39 in KSDB
if socket.gethostname() == 'tumor.jpl.nasa.gov' or socket.gethostname().endswith('.local'):
    _logger.warn(u'Using development KSDB on edrn-dev.jpl.nasa.gov instead of production')
    _rdfBaseURL = u'https://edrn-dev.jpl.nasa.gov/ksdb/publishrdf/?filterby=program&filterval=1&rdftype='
else:
    _rdfBaseURL = u'https://edrn.jpl.nasa.gov/ksdb/publishrdf/?filterby=program&filterval=1&rdftype='

def orderFolderTabs(portal):
    # Members < Working Groups < Resources < News & Meetings < Science Data
    idx = 1
    for i in ('members', 'working-groups', 'resources', 'news-meetings'):
        portal.moveObject(i, idx)
        idx += 1
    ploneUtils = getToolByName(portal, 'plone_utils')
    ploneUtils.reindexOnReorder(portal)

def createKnowledgeFolders(setupTool):
    if setupTool.readDataFile('jpl.mcl.site.knowledge.txt') is None: return
    portal = setupTool.getSite()
    # Don't bother if we're running in the test fixture
    if hasattr(portal._p_jar, 'db') and isinstance(portal._p_jar.db().storage, DemoStorage): return
    if 'resources' not in portal.keys():
        createContentInContainer(
            portal, 'Folder', title=u'Resources',
            description=u'Resources for MCL.'
        )
    if 'archive' not in portal['resources'].keys():
        createContentInContainer(
            portal['resources'], 'Folder', title=u'Archive',
            description=u'Archive for MCL.'
        )
    if 'other-lists' not in portal['resources'].keys():
        createContentInContainer(
            portal['resources'], 'Folder', title=u'Other Lists',
            description=u'Other Lists for MCL.'
        )
    if 'protocols' in portal['resources'].keys():
        move(portal['resources']['protocols'], portal['resources']['archive'])
        rename(portal['resources']['archive']['protocols'], 'Archived Protocols')
    createContentInContainer(
        portal['resources'], 'jpl.mcl.site.knowledge.protocolfolder', title=u'Protocols',
        description=u'MCL Consortium studies',
        url=_rdfBaseURL + u'protocol', ingestEnabled=True
    )
    #members archived
    if 'members' in portal.keys():
        move(portal['members'], portal['resources']['archive'])
        rename(portal['resources']['archive']['members'], 'Archived Members')
    createContentInContainer(
        portal, 'jpl.mcl.site.knowledge.participatingsitefolder', title=u'Members',
        description=u'Hospitals, universities, and other institutions participating with MCL.',
        url=_rdfBaseURL + u'fundedsite', ingestEnabled=True
    )
    if 'publications' in portal['resources'].keys():
        move(portal['resources']['publications'], portal['resources']['archive'])
        rename(portal['resources']['archive']['publications'], 'Archived Publications')
    createContentInContainer(
        portal['resources'], 'jpl.mcl.site.knowledge.publicationfolder', title=u'Publications',
        description=u'Articles and other material published by the MCL Consortium.',
        url=_rdfBaseURL + u'publication', ingestEnabled=True
    )
    institutionfolder = createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.institutionfolder', title=u'Institutions',
        description=u'Universities, hospitals, and other institutions working with the consortium.',
        url=_rdfBaseURL + u'institution', ingestEnabled=True
    )

    #working groups gets removed and replaced
    if 'working-groups' in portal.keys():
        #move(portal['working-groups'], portal['resources']['archive'])
        #rename(portal['resources']['archive']['working-groups'], 'Archived Working Groups')
        #portal.manage_delObjects('working-groups')
        hideTab(portal['working-groups'])
    workingGroup = createContentInContainer(
        portal, 'jpl.mcl.site.knowledge.groupfolder', title=u'Working Groups', id='working-groups-new',
        description=u'Committees and other expert groups appointed to study and report on a particular areas and make recommendations to MCL based on findings.',
        url=_rdfBaseURL + u'group', ingestEnabled=True
    )
    organfolder = createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.organfolder', title=u'Organs',
        description=u'Organs are collections of tissues joined in structural unit to serve a common function.',
        url=_rdfBaseURL + u'organ', ingestEnabled=True
    )
    createContentInContainer(
        portal['resources'], 'jpl.mcl.site.knowledge.personfolder', title=u'People',
        description=u'Individuals working with and comprising the consortium.',
        url=_rdfBaseURL + u'person', ingestEnabled=True
    )
    degreefolder = createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.degreefolder', title=u'Degrees',
        description=u'Academic degrees are qualifications awarded on successful completion of courses of study.',
        url=_rdfBaseURL + u'degree', ingestEnabled=True
    )
    createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.specimentypefolder', title=u'Specimen Types',
        description=u'Specimen Types being studied in MCL.',
        url=_rdfBaseURL + u'specimentype', ingestEnabled=True
    )
    createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.speciesfolder', title=u'Species',
        description=u'Species being studied in MCL.',
        url=_rdfBaseURL + u'species', ingestEnabled=True
    )
    createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.disciplinefolder', title=u'Disciplines',
        description=u'Disciplines being studied in MCL.',
        url=_rdfBaseURL + u'discipline', ingestEnabled=True
    )
    diseasefolder = createContentInContainer(
        portal['resources']['other-lists'], 'jpl.mcl.site.knowledge.diseasefolder', title=u'Diseases',
        description=u'Diseases being studied in MCL.',
        url=_rdfBaseURL + u'disease', ingestEnabled=True
    )
    publish(portal['resources'])
    publish(portal['members'])
    publish(workingGroup)

    registry = getUtility(IRegistry)
    
    #Expose navigations types that this package creates and orders them
    #navigation_settings = registry.forInterface(INavigationSchema, prefix='plone')
    #navigation_settings.displayed_types = ('Folder', 'jpl.mcl.site.knowledge.groupfolder', 'jpl.mcl.site.knowledge.participatingsitefolder')
    #orderFolderTabs(portal)

    registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [
        u'resources/other-lists/organs',
        u'resources/other-lists/diseases',
        u'resources/other-lists/degrees',
        u'resources/other-lists/species',
        u'resources/other-lists/specimen-types',
        u'resources/other-lists/disciplines',
        u'resources/people',
        u'resources/publications',
        u'resources/other-lists/institutions',
        u'members',
        u'resources/protocols',
        u'working-groups'
    ]
