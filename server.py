import os
from flask import Flask
from cfenv import AppEnv
from hdbcli import dbapi

app = Flask(__name__)		
env = AppEnv()		

port = int(os.environ.get('PORT', 3000))
hana = env.get_service(name='hdi-db')	

@app.route('/')
def hello():
    #connect to DB using credentials from hdi-db service
    conn = dbapi.connect(address=hana.credentials['host'],
                         port= int(hana.credentials['port']),
                         user = hana.credentials['user'],
                         password = hana.credentials['password'],
                         CURRENTSCHEMA=hana.credentials['schema'])
    cursor = conn.cursor()

    #execute SQL query
    cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY", {})      
    ro = cursor.fetchone()        #get the first result
    cursor.close()
    conn.close()        #close DB connection

    #return query results
    return "Current time is: " + str(ro["CURRENT_UTCTIMESTAMP"])  

if __name__ == '__main__':
    app.run(port=port)