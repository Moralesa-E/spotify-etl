from datetime import datetime, timedelta
from credentials import Crdentials
from etl import ETL

if __name__=='__main__':
    
    credential = Crdentials()

    processes = ETL()

    sp = credential.credentials_spotify()

    date = datetime.today()-timedelta(days=2)
    data = processes.extract(sp, date)

    data_trans = processes.transform(data)

    url_sql = credential.credentials_mysql("mysql+mysqldb")
    processes.load(data_trans,url_sql)

    data_from_sql = processes.consult_sql_recent_tracks(url_sql)
    data_from_sql.to_csv("rencent_tracks.csv", index=False)