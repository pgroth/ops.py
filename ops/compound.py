from target import *
import urllib2

class Compound:
  def __init__(self, api, compound_uri):
      self.api = api
      self.init_uri = compound_uri
      res = api.getCompoundInfo(compound_uri)
      self._parse_and_populate(res)
      self.json = res

  

  def get_pharmacological_protein_targets(self):
    for i in self.api.getCompoundPharmacology(self.init_uri):
      if "hasAssay" in i:
        if "hasTarget" in i['hasAssay']:
          if type(i['hasAssay']['hasTarget']) is dict:
            tar = i['hasAssay']['hasTarget']
            if tar['type'] == "http://rdf.ebi.ac.uk/terms/chembl#SingleProtein":
              try:
                tar = Target(self.api, tar['_about'])
                yield tar
              except urllib2.HTTPError:
                #print "No Information available for:" + i['hasAssay']['hasTarget']['_about']
                pass
          else:
            for t in i['hasAssay']['hasTarget']:
              if t['type'] == "http://rdf.ebi.ac.uk/terms/chembl#SingleProtein":
                try:
                  tar = Target(self.api, t['_about'])
                  yield tar
                except urllib2.HTTPError:
                  #print "No Information available for:" + t['_about']
                  pass

  def get_pharmacological_targets(self):

     for i in self.api.getCompoundPharmacology(self.init_uri):
        if "hasAssay" in i:
          if "hasTarget" in i['hasAssay']:
            if type(i['hasAssay']['hasTarget']) is dict:
              try:
                tar = Target(self.api, i['hasAssay']['hasTarget']['_about'])
                yield tar
              except urllib2.HTTPError:
                #print "No Information available for:" + i['hasAssay']['hasTarget']['_about']
                pass
            else:
              for t in i['hasAssay']['hasTarget']:
                try:
                   tar = Target(self.api, t['_about'])
                   yield tar
                except urllib2.HTTPError:
                  #print "No Information available for:" + t['_about']
                  pass


  def _parse_and_populate(self, compound_info_results):
    primaryTopic = compound_info_results['result']['primaryTopic']
    self._item_parse(primaryTopic)

    exactMatches = primaryTopic['exactMatch']

    for exactMatch in exactMatches:
      self._item_parse(exactMatch)


  def _item_parse(self, item):
       if "prefLabel" in item:
         self.label = item['prefLabel']

       if "biotransformation" in item:
         self.biotransformation = item["biotransformation"]

       if "drugType" in item:
         self.drugType = item['drugType']

       if "genericName" in item:
         self.genericName = item['genericName']

       if "proteinBinding" in item:
         self.proteinBinding = item['proteinBinding']

       if "mw_freebase" in item:
         self.molecular_weight = item['mw_freebase']

       if "toxicity" in item:
         self.toxicity = item['toxicity']

       if "inchi" in item:
         self.inchi = item['inchi']

       if "inchikey" in item:
         self.inchi_key = item["inchikey"]

       if "hba" in item:
         self.number_hbond_acceptors = item['hba']

       if "hbd" in item:
         self.number_hbond_donors = item['hbd']

       if "logp" in item:
         self.alogp = item['logp']

       if "molformula" in item:
         self.molecular_formula = item['molformula']

       if "molweight" in item:
         self.molecular_weight = item['molweight']

       if "psa" in item:
         self.polar_surface_area = item['psa']

       if "ro5_violations" in item:
         self.rule_of_5_violations = item['ro5_violations']

       if "rtb" in item:
         self.rotatable_bonds = item['rtb']

       if "smiles" in item:
         self.smiles = item['smiles']
