class Target:
  def __init__(self, api, compound_info_results):
      self.api = api
      self._parse_and_populate(compound_info_results)

  def _parse_and_populate(self, compound_info_results):
    primaryTopic = compound_info_results['result']['primaryTopic']
    if "prefLabel" in primaryTopic:
      self.label = primaryTopic['prefLabel']

    exactMatches = primaryTopic['exactMatch']

    for exactMatch in exactMatches:
      if "numberOfResidues" in exactMatch:
        self.number_of_residues = exactMatch["numberOfResidues"]

      if "Function_Annotation" in exactMatch:
        self.function_annotation = exactMatch["Function_Annotation"]

      if "organisim" in exactMatch:
        self.organism_url = exactMatch["organisim"]
