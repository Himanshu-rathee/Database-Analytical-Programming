import urllib.request as urllib
url = 'https://catalogue.data.govt.nz/api/3/action/datastore_search?resource_id=0262a12a-b0bb-4b31-aa32-736c06b3c319&limit=5&q=title:jones'
fileobj = urllib.urlopen(url)
print(fileobj.read())