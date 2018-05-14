# encoding: utf-8

u'''JPL MCL Site Knowledge — setup handlers.'''

from ._utils import publish, hideTab, rename, move
from plone.dexterity.utils import createContentInContainer
from plone.registry.interfaces import IRegistry
from ZODB.DemoStorage import DemoStorage
from zope.component import getUtility
import socket, logging, plone.api

_logger = logging.getLogger(__name__)


# There has to be a better way of doing this:
# MCL ID is currently 39 in KSDB
if socket.gethostname() == 'tumor.jpl.nasa.gov' or socket.gethostname().endswith('.local'):
    _logger.warn(u'Using development KSDB on edrn-dev.jpl.nasa.gov instead of production')
    _rdfBaseURL = u'https://edrn-dev.jpl.nasa.gov/ksdb/publishrdf/?filterby=program&filterval=1&rdftype='
else:
    _rdfBaseURL = u'https://mcl.jpl.nasa.gov/ksdb/publishrdf/?filterby=program&filterval=1&rdftype='


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

    if 'archive' not in portal.keys():
        createContentInContainer(
            portal, 'Folder', title=u'Archive',
            description=u'Archive for MCL.'
        )
        hideTab(portal['archive'])
    # Nuke resource folders not being used
    if 'datasets' in portal['resources'].keys():
        plone.api.content.delete(obj=portal['resources']['datasets'])
    if 'image-data' in portal['resources'].keys():
        plone.api.content.delete(obj=portal['resources']['image-data'])
    if 'pathology-data' in portal['resources'].keys():
        plone.api.content.delete(obj=portal['resources']['pathology-data'])

    if 'other-lists' not in portal['archive'].keys():
        createContentInContainer(
            portal['archive'], 'Folder', title=u'Other Lists',
            description=u'Other Lists for MCL.'
        )
    if 'protocols' in portal['resources'].keys():
        move(portal['resources']['protocols'], portal['archive'])
        rename(portal['archive']['protocols'], 'Archived Protocols')
    createContentInContainer(
        portal['resources'], 'jpl.mcl.site.knowledge.protocolfolder', title=u'Protocols',
        description=u'MCL Consortium studies',
        url=_rdfBaseURL + u'protocol', ingestEnabled=True
    )
    #members archived
    if 'members' in portal.keys():
        move(portal['members'], portal['archive'])
        rename(portal['archive']['members'], 'Archived Members')
    createContentInContainer(
        portal, 'jpl.mcl.site.knowledge.participatingsitefolder', title=u'Members',
        description=u'Hospitals, universities, and other institutions participating with MCL.',
        url=_rdfBaseURL + u'fundedsite', ingestEnabled=True
    )
    if 'publications' in portal['resources'].keys():
        move(portal['resources']['publications'], portal['archive'])
        rename(portal['archive']['publications'], 'Archived Publications')
    publication = createContentInContainer(
        portal, 'jpl.mcl.site.knowledge.publicationfolder', title=u'Publications',
        description=u'Articles and other material published by the MCL Consortium.',
        url=_rdfBaseURL + u'publication', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.institutionfolder', title=u'Institutions',
        description=u'Universities, hospitals, and other institutions working with the consortium.',
        url=_rdfBaseURL + u'institution', ingestEnabled=True
    )

    # working groups cannot be removed for some reason, so will just hide for now
    # [kelly/2017-05-01] THIS IS SO WEIRD
    if 'working-groups' in portal.keys():
        hideTab(portal['working-groups'])
    workingGroup = createContentInContainer(
        portal, 'jpl.mcl.site.knowledge.groupfolder', title=u'Working Groups', id='working-groups-new',
        description=u'Committees and other expert groups appointed to study and report on a particular areas and make recommendations to MCL based on findings.',
        url=_rdfBaseURL + u'group', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.organfolder', title=u'Organs',
        description=u'Organs are collections of tissues joined in structural unit to serve a common function.',
        url=_rdfBaseURL + u'organ', ingestEnabled=True
    )
    createContentInContainer(
        portal['resources'], 'jpl.mcl.site.knowledge.personfolder', title=u'People',
        description=u'Individuals working with and comprising the consortium.',
        url=_rdfBaseURL + u'person', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.degreefolder', title=u'Degrees',
        description=u'Academic degrees are qualifications awarded on successful completion of courses of study.',
        url=_rdfBaseURL + u'degree', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.specimentypefolder', title=u'Specimen Types',
        description=u'Specimen Types being studied in MCL.',
        url=_rdfBaseURL + u'specimentype', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.speciesfolder', title=u'Species',
        description=u'Species being studied in MCL.',
        url=_rdfBaseURL + u'species', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.disciplinefolder', title=u'Disciplines',
        description=u'Disciplines being studied in MCL.',
        url=_rdfBaseURL + u'discipline', ingestEnabled=True
    )
    createContentInContainer(
        portal['archive']['other-lists'], 'jpl.mcl.site.knowledge.diseasefolder', title=u'Diseases',
        description=u'Diseases being studied in MCL.',
        url=_rdfBaseURL + u'disease', ingestEnabled=True
    )
    publish(portal['resources'])
    publish(portal['members'])
    publish(workingGroup)
    publish(publication)

    registry = getUtility(IRegistry)

    registry['jpl.mcl.site.knowledge.interfaces.ISettings.objects'] = [
        u'archive/other-lists/organs',
        u'archive/other-lists/diseases',
        u'archive/other-lists/degrees',
        u'archive/other-lists/species',
        u'archive/other-lists/specimen-types',
        u'archive/other-lists/disciplines',
        u'resources/people',
        u'publications',
        u'archive/other-lists/institutions',
        u'members',
        u'resources/protocols',
        u'working-groups-new'
    ]
