class Compound:
  def __init__(self, api, compound_info_results):
      self.api = api
      self._parse_and_populate(compound_info_results)

  def _parse_and_populate(self, compound_info_results):

    primaryTopic = compound_info_results['result']['primaryTopic']
    if "prefLabel" in primaryTopic:
      self.label = primaryTopic['prefLabel']

    exactMatches = primaryTopic['exactMatch']

    for exactMatch in exactMatches:
       if "biotransformation" in exactMatch:
         self.biotransformation = exactMatch["biotransformation"]

       if "drugType" in exactMatch:
         self.drugType = exactMatch['drugType']

       if "genericName" in exactMatch:
         self.genericName = exactMatch['genericName']

       if "proteinBinding" in exactMatch:
         self.proteinBinding = exactMatch['proteinBinding']

       if "mw_freebase" in exactMatch:
         self.molecular_weight = exactMatch['mw_freebase']

       if "toxicity" in exactMatch:
         self.toxicity = exactMatch['toxicity']

       if "inchi" in exactMatch:
         self.inchi = exactMatch['inchi']

       if "inchikey" in exactMatch:
         self.inchi_key = exactMatch["inchikey"]

       if "hba" in exactMatch:
         self.number_hbond_acceptors = exactMatch['hba']

       if "hbd" in exactMatch:
         self.number_hbond_donors = exactMatch['hbd']

       if "logp" in exactMatch:
         self.alogp = exactMatch['logp']

       if "molformula" in exactMatch:
         self.molecular_formula = exactMatch['molformula']

       if "molweight" in exactMatch:
         self.molecular_weight = exactMatch['molweight']

       if "psa" in exactMatch:
         self.polar_surface_area = exactMatch['psa']

       if "ro5_violations" in exactMatch:
         self.rule_of_5_violations = exactMatch['ro5_violations']

       if "rtb" in exactMatch:
         self.rotatable_bonds = exactMatch['rtb']

       if "smiles" in exactMatch:
         self.smiles = exactMatch['smiles']
