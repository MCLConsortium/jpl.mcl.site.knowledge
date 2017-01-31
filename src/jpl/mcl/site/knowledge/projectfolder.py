# encoding: utf-8

u'''MCL — Project Folder'''

from ._base import IIngestableFolder, Ingestor, IngestableFolderView
from .project import IProject
from five import grok


class IProjectFolder(IIngestableFolder):
    u'''Folder containing projects.'''


class ProjectIngestor(Ingestor):
    u'''RDF ingestor for instutitions.'''
    grok.context(IProjectFolder)
    def getContainedObjectInterface(self):
        return IProject


class View(IngestableFolderView):
    u'''View for an institution folder'''
    grok.context(IProjectFolder)