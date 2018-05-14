# encoding: utf-8

u'''MCL — Publication'''

from interfaces import IPublication, IPerson


IPublication.setTaggedValue('typeURI', u'https://cancer.jpl.nasa.gov/rdf/types.rdf#Publication')
IPublication.setTaggedValue('predicateMap', {
    u'http://purl.org/dc/terms/title': ('title', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#year': ('year', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#author': ('author', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#pmid': ('pmid', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#pi': ('pi', False),
    u'https://cancer.jpl.nasa.gov/rdf/schema.rdf#journal': ('journal', False)
})
IPublication.setTaggedValue('fti', 'jpl.mcl.site.knowledge.publication')
