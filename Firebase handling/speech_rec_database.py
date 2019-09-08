from firebase import firebase
import firebase_admin
import pandas as pd
import json
import csv
import datetime
import requests
#import wget
from firebase_admin import credentials
from firebase_admin import storage


firebase = firebase.FirebaseApplication('https://bankappvrec.firebaseio.com/')

result = firebase.get('',None)

#print(result)

# Fetch the service account key JSON file contents
cred = credentials.Certificate("credentials2.json")

# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'bankappvrec.appspot.com',
}, name='storage')

bucket = storage.bucket(app=app)


#print(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))

#url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
#myfile = requests.get(url)
#open('aud1.3gp', 'wb').write(myfile.content)

row = ['acc_no','email_id','name','password','audio']
with open('f4.csv','a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(row)
    for i in result:
    	a = []
    	a.append(i)
    	a.append(result[i]['Main Details']['email_id'])
    	a.append(result[i]['Main Details']['name'])
    	a.append(result[i]['Main Details']['password'])
    	blob = bucket.blob(i + "/audio_file_1")
    	url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')
    	myfile = requests.get(url)

    	open('audio_files/' + i + '.3gp', 'wb').write(myfile.content)
    	a.append('audio_files/' + i)

    	writer.writerow(a)


