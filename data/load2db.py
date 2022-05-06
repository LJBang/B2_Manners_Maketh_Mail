import pandas as pd
import numpy as np
import psycopg2
import sys
import glob

import sqlalchemy
from sqlalchemy import create_engine

try:
    engine = create_engine("postgresql://greetings:12321@localhost:5432/greetings")
except:
    print('db connection fail')
    sys.exit()

'''
try:
    conn = psycopg2.connect(host='localhost', port=5432,
    dbname="greetings",
    user="greetings", password="12321")
except:
    print("db connection fail")
    sys.exit()
'''
dir = '/home/ubuntu/B2_Greetings/data/csv_data/'
target = ['opening','closing']

with open(dir+'qualitycc.txt', 'w') as file:
    file.write('list of csv dataset with NaN \n')

def nancheck(fname):
    df = pd.read_csv(fname).drop('Unnamed: 0', axis=1)
    if len(df[df.isnull()])!=0:
        with open(dir+'qualitycc.txt', 'a') as file:
            file.write(fname+'\n')
        df = df.dropna(axis=0)
        df = df.reset_index().drop('index', axis=1)
    return df

def float2int(df, clist):
    for column in clist:
        df[column] = df[column].astype('int32')
    return df

flist = glob.glob(dir+target[0]+'/*.csv')
df = nancheck(flist[0])
df = float2int(df, ['label','class0 id','class1 id'])
for f in flist[1:]:
    df = pd.concat([df, float2int(nancheck(f), ['label','class0 id','class1 id'])], 
    ignore_index=True)
flist = glob.glob(dir+target[1]+'/*.csv')
for f in flist:
    df = pd.concat([df, float2int(nancheck(f), ['label','class0 id','class1 id'])], 
    ignore_index=True)

df.rename(columns = lambda x: x.replace(' ','_'),inplace=True)

engine.execute("DROP TABLE IF EXISTS public.train;")

df.to_sql(name = 'train',
    con = engine,
    schema = 'public',
    index = True,
    index_label = 'data_id',
    dtype = {
            'data_id': sqlalchemy.types.INTEGER(),
            'label': sqlalchemy.types.INTEGER(),
            'class0_id': sqlalchemy.types.INTEGER(),
            'class0_name': sqlalchemy.types.VARCHAR(10),
            'class1_id': sqlalchemy.types.INTEGER(),
            'class1_name': sqlalchemy.types.VARCHAR(10),
            'keyword': sqlalchemy.types.VARCHAR(40),
            'sentence': sqlalchemy.types.VARCHAR(300)
            }
        )

engine.execute("ALTER TABLE public.train ADD PRIMARY KEY (data_id);")
