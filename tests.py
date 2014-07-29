import ops

def basic_test():
  api = ops.API('0e939a76', '1004d9ef5f4ee1ab0bbfc02b623cb955')
  json = api.getCompoundInfo('http://www.conceptwiki.org/concept/38932552-111f-4a4e-a46a-4ed1d7bdf9d5')
  #print json
  compound = ops.Compound(api, json)
  print dir(compound)
  print(compound.label)

  #for i in api.getCompoundPharmacology("http://www.conceptwiki.org/concept/dd85c868-74be-4b86-ae58-12ac6d19a4ba"):
  #    print i['_about']

  targetJson = api.getTargetInfo('http://www.conceptwiki.org/concept/00059958-a045-4581-9dc5-e5a08bb0c291')

  target = ops.Target(api, targetJson)

  print dir(target)
  print(target.function_annotation)
  print(target.label)

basic_test()
