import urllib
import json
url = 'http://dati.openexpo2015.it/catalog/api/action/datastore_search?resource_id=1ee3ea1b-58e3-48bf-8eeb-36ac313eeaf8&limit=3'
fileobj = urllib.urlopen(url)
s =  fileobj.read()
d = json.loads(s)
result = d['result']
records = result['records']
for prova in records:
	print prova['_id']