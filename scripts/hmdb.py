# obtain all kegg identifiers from all hmdb identifiers in latest HMDB database
# requires to download "All Metabolites" dataset from https://hmdb.ca/downloads, in XML format
# latest release: Current version 5.0 Released on 2021-11-17
# thanks to yufree :  https://gist.github.com/yufree/f552d865096010445fc7b969e7e9d439
# credits: yufree

from io import StringIO
from lxml import etree
import csv
xml = 'hmdb_metabolites.xml'

ns = {'hmdb': 'http://www.hmdb.ca'}

context = etree.iterparse(xml, tag='{http://www.hmdb.ca}metabolite')

csvfile = open('../tables/hmdb.csv', 'w')
fieldnames = ['omim', 'dname', 'smpdb', 'keggmap', 'accession', 'monisotopic_molecular_weight', 'iupac_name', 'name', 'chemical_formula', 'InChIKey', 'cas_registry_number', 'kegg', 'food','drugbank','drugbankmet', 'biocyc', 'pubchem', 'chemspider', 'smiles', 'metlin_id', 'kingdom', 'direct_parent', 'super_class', 'class', 'sub_class', 'molecular_framework', 'logpexp']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

for event, elem in context:

    try:
        omim = elem.xpath('hmdb:diseases/hmdb:disease/hmdb:omim_id/text()', namespaces=ns)
    except:
        omim = 'NA'
    try:
        dname = elem.xpath('hmdb:diseases/hmdb:disease/hmdb:name/text()', namespaces=ns)
    except:
        dname = 'NA'
    try:
        smpdb = elem.xpath('hmdb:pathways/hmdb:pathway/hmdb:smpdb_id/text()', namespaces=ns)
    except:
        smpdb = 'NA'
    try:
        keggmap = elem.xpath('hmdb:pathways/hmdb:pathway/hmdb:kegg_map_id/text()', namespaces=ns)
    except:
        keggmap = 'NA'

    accession = elem.xpath('hmdb:accession/text()', namespaces=ns)[0]
    try:
        monisotopic_molecular_weight = elem.xpath('hmdb:monisotopic_molecular_weight/text()', namespaces=ns)[0]
    except:
        monisotopic_molecular_weight = 'NA'
    try:
        iupac_name = elem.xpath('hmdb:iupac_name/text()', namespaces=ns)[0].encode('utf-8')
    except:
        iupac_name = 'NA'
    name = elem.xpath('hmdb:name/text()', namespaces=ns)[0].encode('utf-8')
    try:
        chemical_formula = elem.xpath('hmdb:chemical_formula/text()', namespaces=ns)[0]
    except:
        chemical_formula = 'NA'
    try:
        inchikey = elem.xpath('hmdb:inchikey/text()', namespaces=ns)[0]
    except:
        inchikey = 'NA'
    try:
        cas_registry_number = elem.xpath('hmdb:cas_registry_number/text()', namespaces=ns)[0]
    except:
        cas_registry_number = 'NA'
    try:
        kegg = elem.xpath('hmdb:kegg_id/text()', namespaces=ns)[0]
    except:
        kegg = 'NA'
    try:
        food = elem.xpath('hmdb:foodb_id/text()', namespaces=ns)[0]
    except:
        food = 'NA'
    try:
        drugbank = elem.xpath('hmdb:drugbank_id/text()', namespaces=ns)[0]
    except:
        drugbank = 'NA'
    try:
        drugbankmet = elem.xpath('hmdb:drugbank_metabolite_id/text()', namespaces=ns)[0]
    except:
        drugbankmet = 'NA'
    try:
        biocyc = elem.xpath('hmdb:biocyc_id/text()', namespaces=ns)[0]
    except:
        biocyc = 'NA'
    try:
        pubchem = elem.xpath('hmdb:pubchem_compound_id/text()', namespaces=ns)[0]
    except:
        pubchem = 'NA'
    try:
        chemspider = elem.xpath('hmdb:chemspider_id/text()', namespaces=ns)[0]
    except:
        chemspider = 'NA'
    try:
        smiles = elem.xpath('hmdb:smiles/text()', namespaces=ns)[0]
    except:
        smiles = 'NA'
    try:
        metlin_id = elem.xpath('hmdb:metlin_id/text()', namespaces=ns)[0]
    except:
        metlin_id = 'NA'
    try:
        logpexp = elem.xpath('hmdb:experimental_properties/hmdb:property[hmdb:kind ="logp"]/hmdb:value/text()', namespaces=ns)[0]
    except:
        logpexp = 'NA'
    try:
        kingdom = elem.xpath('hmdb:taxonomy/hmdb:kingdom/text()', namespaces=ns)[0]
    except:
        kingdom = 'NA'
    try:
        direct_parent = elem.xpath('hmdb:taxonomy/hmdb:direct_parent/text()', namespaces=ns)[0]
    except:
        direct_parent = 'NA'
    try:
        super_class = elem.xpath('hmdb:taxonomy/hmdb:super_class/text()', namespaces=ns)[0]
    except:
        super_class = 'NA'
    try:
        classorg = elem.xpath('hmdb:taxonomy/hmdb:class/text()', namespaces=ns)[0]
    except:
        classorg = 'NA'
    try:
        sub_class = elem.xpath('hmdb:taxonomy/hmdb:sub_class/text()', namespaces=ns)[0]
    except:
        sub_class = 'NA'
    try:
        molecular_framework = elem.xpath('hmdb:taxonomy/hmdb:molecular_framework/text()', namespaces=ns)[0]
    except:
        molecular_framework = 'NA'

    writer.writerow({'omim': omim, 'dname': dname, 'smpdb': smpdb, 'keggmap': keggmap, 'accession': accession, 'monisotopic_molecular_weight': monisotopic_molecular_weight, 'iupac_name': iupac_name, 'name': name, 'chemical_formula': chemical_formula, 'InChIKey': inchikey, 'cas_registry_number': cas_registry_number, 'kegg': kegg, 'food': food, 'drugbank': drugbank, 'drugbankmet': drugbankmet,'biocyc': biocyc, 'pubchem': pubchem, 'chemspider': chemspider, 'smiles': smiles, 'metlin_id': metlin_id, 'kingdom': kingdom, 'direct_parent': direct_parent, 'super_class': super_class, 'class': classorg, 'sub_class': sub_class, 'molecular_framework': molecular_framework, 'logpexp': logpexp})
    # It's safe to call clear() here because no descendants will be
    # accessed
    elem.clear()
# Also eliminate now-empty references from the root node to elem
    for ancestor in elem.xpath('ancestor-or-self::*'):
        while ancestor.getprevious() is not None:
            del ancestor.getparent()[0]
del context
