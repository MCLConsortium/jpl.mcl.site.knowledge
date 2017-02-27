# encoding: utf-8

u'''MCL — Disease Folder'''

from ._base import IIngestableFolder, Ingestor, IngestableFolderView
from .disease import IDisease
from five import grok


class IDiseaseFolder(IIngestableFolder):
    u'''Folder containing body systems, also known as diseases.'''


class DiseaseIngestor(Ingestor):
    u'''RDF ingestor for diseases.'''
    grok.context(IDiseaseFolder)
    def getContainedObjectInterface(self):
        return IDisease


class View(IngestableFolderView):
    u'''View for an disease folder'''
    grok.context(IDiseaseFolder)
