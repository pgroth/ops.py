

class Target:
  def __init__(self, api, target_uri):
      self.api = api
      self.init_uri = target_uri
      res = api.getTargetInfo(target_uri)
      self._parse_and_populate(res)
      self.json = res

  ##todo: filter out duplicates
  def get_active_compounds(self):
      from compound import Compound
      for i in self.api.getTargetPharmacology(self.init_uri):
        compound_url = i['hasMolecule']['_about']
        c = Compound(self.api, compound_url)
        yield c

  def _parse_and_populate(self, compound_info_results):
    primaryTopic = compound_info_results['result']['primaryTopic']
    self._item_parse(primaryTopic)

    exactMatches = primaryTopic['exactMatch']

    for exactMatch in exactMatches:
      self._item_parse(exactMatch)


  def _item_parse(self, item):
    if "prefLabel" in item:
      self.label = item['prefLabel']
    elif "label" in item:
      self.label = item['label']

    if "type" in item:
      self.type = item['type']

    if "numberOfResidues" in item:
      self.number_of_residues = item["numberOfResidues"]

    if "Function_Annotation" in item:
      self.function_annotation = item["Function_Annotation"]

    if "organisim" in item:
      self.organism_url = item["organisim"]
