import logging
import csv
import json
import requests
import os
from requests.auth import HTTPBasicAuth

import azure.functions as func


ArtifactoryUrl= os.getenv['ARTIFACTORYURL']
Bearer_token= os.getenv['Bearer_token']
url = ArtifactoryUrl+"/api/storageinfo"
payload={}



print ("url : " + url);



#response = requests.request("GET", url, data=payload)
headers = {"Authorization": "Bearer {}".format(Bearer_token)}
response = requests.get(url, headers=headers,data=payload)
payloadList = response.json



print(response.content)

database = 'govframework'

username = 'gfatadmin@govframework'

password = 'Password@1234'

server = 'govframework.database.windows.net'


port = os.getenv('PORT',default=1433);driver = '{ODBC Driver 13 for SQL Server}'#connect using parsed URL

odbc_str = 'DRIVER='+driver;'SERVER=';+server;'PORT='+port;'DATABASE='+database+';UID='+username+';PWD='+ password

connect_str = 'mssql+pyodbc:///?odbc_connect=' + quote_plus(odbc_str)#connect with sa url format

sa_url = f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver={driver}";engine = create_engine(connect_str/sa_url);print(engine.execute('''

                         YOUR SQL QUERY

                     ''').fetchall())