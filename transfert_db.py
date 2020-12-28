import os
import pandas as pd
import numpy as np
import sqlite3
import json

path_directory = '/media/jarvis/OS/Users/Leclerc/Desktop/finca'
db_directory = '/home/jarvis/Bureau/Fun/finca/finca_db/project/db.sqlite'

def transfert(table_path, names_list):
    table_name = table_path.capitalize().replace('.csv','')
    csv = pd.read_csv(os.path.join(path_directory, table_path), names = names_list)
    csv = csv[1::]
    
    print(csv.head())

    csv = np.array(csv)

    conn = sqlite3.connect(db_directory)
    c = conn.cursor()

    c.execute("DELETE FROM {table}".format(table = table_name))
    conn.commit()

    col = str(names_list).replace('[','').replace(']', '').replace("'", '').replace(' ', '')
    colPoints = ':' + col.replace(',', ',:')
    cmd = "INSERT INTO {table}({col}) VALUES ({colPoints})".format(table = table_name, col = col, colPoints = colPoints)
    for line in csv:
        data = dict()
        for i, name in enumerate(names_list):
                data[name] = line[i]
        c.execute(cmd, data)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    with open('db.json') as json_file:
        table_list = json.load(json_file)
    print(table_list)
    for table in table_list:
        transfert(table['table_name'],table['names_list'])