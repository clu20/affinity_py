'''
	Running this will get the list entry data in a JSON format
	Add a new list entry into Deals with 
	Name: Fun times
	URL: funtimes.com
	Changing the status to won is done on the web browser application itself.
'''
import requests

url = "https://api.affinity.co"
auth = 'on08W1hEdvo5BTv4C3dx892Cdc_xzL9i79clBZvnlgU'

#Gets list id
#Because for this exercise there is only one list we just grab the first one
def getlistId(url, auth):
	response = requests.get(url+'/lists', auth=('',auth))
	#print(response.json())
	return response.json()[0]['id']

#Gets all list entries for the specified listid
def getlistEntry(listid, url, auth):
	response = requests.get(url+'/lists/'+listid+'/list-entries', auth=('',auth))
	#print(url+'/lists/'+listid+'/list-entries')
	return response.json()

#Add list entry to specific listid
def addlistEntry(listid,data,url,auth):
	response = requests.post(url+'/lists/'+listid+'/list-entries',auth=('',auth),data = data)
	#print(url+'/lists/'+listid+'/list-entries')
	return response.text

#Because the list is a list of organizations
#We create the new entity as an organization
def createOrganization(data,url,auth):
	response = requests.post(url+'/organizations', data=data, auth=('',auth))
	#return response.text
	print(response.text)
	return response.json()['id']

listid = getlistId(url, auth)
print(getlistEntry(str(listid),url,auth))

#Below are the steps taken in python to add the new list entry
#Changing the status to won was done on the browser application
#Does not delete the already added and status changed Fun Times that needs to be
#done separately or you'll just continously add organizations of Fun Times.
dataorg = {
	'name': "Fun Times",
	'domain': 'funtimes.com'
}
'''
entityid = createOrganization(dataorg,url,auth)

datalistentry = {
	'entity_id' :entityid
}
print(addlistEntry(str(listid), datalistentry, url, auth))
'''

#Mimic Customer issue call with data provided
'''data={}
r = requests.put("https://api.affinity.co/organizations/283512094?person_id=87870208", auth=('',auth),data=data)
print(r.text)'''

