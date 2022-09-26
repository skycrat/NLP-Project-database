from asyncore import read
import datetime
from distutils.log import debug
import logging
from plistlib import UID
from sre_constants import SUCCESS
import pandas as pd
import pyodbc
import json

import azure.functions as func

CONFIG = json.load(open("TimerTrigger01/config.json"))


class DatabaseLinker():
    def __init__(self, conn_string):
        self.conn=pyodbc.connect(conn_string)
        self.cursor=self.conn.cursor()
        print(pyodbc.drivers())

    @staticmethod 
    def create_conn_string(server,user,database,password,driver="ODBC Driver 17for SQL Server"):   #ODBC Driver 12 for 
        return f'DRIVER={driver};SERVER={server};DATABASE={database};USER={user};PASSWORD={password}'
        

    def send_query(self,query):
        
        row = self.cursor.execute(query)
        results = []
        
        for i in row:
            results.append(i)
        
        return results

def source():
    
    #Connect to database
    db_creds = CONFIG["credentials"]["database"]
    
    conn_string = DatabaseLinker.create_conn_string(
        db_creds["server"],
        db_creds["user"],
        db_creds["password"],
        db_creds["database"]
    )
    
    db_linker = DatabaseLinker(conn_string)
    
    print("conectada existosamente a la base de datos")
    
    print(db_linker.send_query("SELECT * FROM dbo.Prueba"))
    
    df = pd.read_csv("TimerTrigger01/WinesData.csv", sep= ";")
    df = df.iloc[::5]
    
    print(df.sample(1))  

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

source()

