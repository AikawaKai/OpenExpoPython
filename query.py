import urllib
import json
url = 'http://dati.openexpo2015.it/catalog/api/action/datastore_search?resource_id=34e298ad-3a99-4feb-9614-b9c4071b9d8e&limit=10000'
fileobj = urllib.urlopen(url)
azienda = (raw_input("Inserisci il nome dell'azienda che vuoi cercare: ")).lower()
s =  fileobj.read()
d = json.loads(s)
result = d['result']
records = result['records']
resultquerystring = '\nImporto appalti '+azienda+'\n\n'
for prova in records:
	if ((prova['Aggiudicatario']).lower()).find(azienda)!=-1:
		    resultquerystring = 'n'+resultquerystring +'Importo totale attuazione sicurezza: '+prova['Importo totale attuazione sicurezza']+'\n'+'Importo totale somme a disposizione: '+prova['Importo totale somme a disposizione']+'\n'+'Cantiere: '+prova['Cantiere']+'\n'+'Stato: '+prova['Stato']+'\n'+'Aggiudicatario: '+prova['Aggiudicatario']+'\n'+'Importo componente lavori: '+prova['Importo componente lavori']+'\n'+'Oggetto del lotto: '+prova['Oggetto del lotto']+'\n'+'Importo progettazione: '+prova['Importo progettazione']+'\n'+'Numero gara: '+prova['Numero gara']+'\n'+'Importo componente servizi: '+prova['Importo componente servizi']+'\n'+'Somme non assoggettate a ribasso: '+prova['Somme non assoggettate a ribasso']+'\n'+'Importo componente forniture: '+prova['Importo componente forniture']+'\n'+'Importo complessivo intervento: '+prova['Importo complessivo intervento']+'\n'+'Importo complessivo appalto: '+prova['Importo complessivo appalto']+'\n'+'Oggetto della gara: '+prova['Oggetto della gara']+'\n'+'ID lotto: '+prova['ID lotto']+'\n\n\n'

print resultquerystring
with open('Appalti '+azienda+".txt", "w") as text_file:
    text_file.write(resultquerystring)

#to do: query per subappalti 