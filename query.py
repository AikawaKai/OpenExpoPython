import urllib
import json
url = 'http://dati.openexpo2015.it/catalog/api/action/datastore_search?resource_id=34e298ad-3a99-4feb-9614-b9c4071b9d8e&limit=10000'
fileobj = urllib.urlopen(url)
azienda = (raw_input("Inserisci il nome dell'azienda che vuoi cercare: ")).lower()
s =  fileobj.read()
d = json.loads(s)
result = d['result']
records = result['records']
resultquerystring = ''
for prova in records:
	if ((prova['Aggiudicatario']).lower()).find(azienda)!=-1:
		resultquerystring =resultquerystring+ 'Cantiere: '+prova['Cantiere']+'\nAzienda: '+prova['Aggiudicatario'] + '\nImporto complessivo appalto: '+prova['Importo complessivo appalto']+'\n\n'

print resultquerystring
with open(azienda+".txt", "w") as text_file:
    text_file.write(resultquerystring)