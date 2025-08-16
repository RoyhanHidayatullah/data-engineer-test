import pandas as pd
from sqlalchemy import create_engine
import os
import time

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

time.sleep(10) 

try:
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
    print("Connection to PostgreSQL DB successful")

    events_path = 'data/CRMEvents.csv'
    call_logs_path = 'data/CRMCallCenterLogs.csv'

    df_events = pd.read_csv(events_path)
    df_call_logs = pd.read_csv(call_logs_path)
    print("CSV files read successfully.")

    df_events.columns = df_events.columns.str.replace(' ', '_').str.lower()
    df_call_logs.columns = df_call_logs.columns.str.replace(' ', '_').str.lower()
    
    df_events['date_received'] = pd.to_datetime(df_events['date_received'])
    df_events['date_sent_to_company'] = pd.to_datetime(df_events['date_sent_to_company'])

    df_events.to_sql('crm_events', engine, if_exists='replace', index=False)
    print("CRMEvents data loaded successfully into 'crm_events' table.")

    df_call_logs.to_sql('crm_call_center_logs', engine, if_exists='replace', index=False)
    print("CRMCallCenterLogs data loaded successfully into 'crm_call_center_logs' table.")

except Exception as e:
    print(f"An error occurred: {e}")