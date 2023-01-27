import os
import numpy as np
import pandas as pd
import mysql.connector

class DataHandler:
    def __init__(self,columns=None,dtypes=None,is_SQL=False,SQL_handle=None,table_name=None):
        self.columns=columns
        self.dtypes=dtypes
        self.is_SQL=is_SQL
        self.SQL_handle=SQL_handle
        self._setup(table_name)

    def _setup(self,table_name):
        if not self.is_SQL:
            self.table=pd.DataFrame(columns=self.columns)
        else:
            self.table_name=self.SQL_handle.hasTable(tabname=table_name,columns=self.columns,dtypes=self.dtypes)
    
    @property
    def Count(self):
        if not self.is_SQL:
            return self.table.shape[0]
        else:
            return self.SQL_handle.Count(self.table_name)

    def Insert(self,row):
        if not self.is_SQL:
            self.table.loc[self.table.shape[0]]=row
        else:
            self.SQL_handle.Insert(self.table_name,[row])

    def Update(self,idx,col,val):
        if not self.is_SQL:
            self.table.loc[idx,col]=val
        else:
            self.SQL_handle.setVal(self.table_name,idx,col,val)

    def GetAT(self,idx,col):
        if not self.is_SQL:
            return self.table.loc[idx,col]
        else:
            return self.SQL_handle.getVal(self.table_name,idx,col)

    def IncrementBy(self,idx,col,by):
        if not self.is_SQL:
            self.table.loc[idx,col]+=by
        else:
            self.SQL_handle.IncrementBy(self.table_name,idx,col,by)


class SQLHandler:
    def __init__(self,host='localhost',user='root',password='abc',db='dQdb'):
        connected=False
        while not connected:
            try:
                self.mydb = mysql.connector.connect(host=host,user=user,password=password)
                connected=True
            except:
                pass
        self.mycursor = self.mydb.cursor()
        self._setup(db)
        
    def _setup(self,db):
        self.UseDB(db)

    def UseDB(self,dbname=None):
        self.mycursor.execute("SHOW DATABASES")
        if dbname not in [r[0] for r in self.mycursor]:
            self.mycursor.execute(f"CREATE DATABASE {dbname}")
        self.mycursor.execute(f"USE {dbname}")

    def DropDB(self,dbname=None):
        self.mycursor.execute("SHOW DATABASES")
        if dbname in [r[0] for r in self.mycursor]:
            self.mycursor.execute(f"DROP DATABASE {dbname}")
        self.mydb.commit()

    def hasTable(self,tabname=None,columns=None,dtypes=None):
        self.mycursor.execute("SHOW TABLES")
        if tabname not in [r[0] for r in self.mycursor]:
            dmap={'int':'INT','str':'VARCHAR(32)'}
            col_config=''
            for c,d in zip(columns,dtypes):
                col_config+=f", {c} {dmap[d]}"
            self.mycursor.execute(f"CREATE TABLE {tabname} (id INT AUTO_INCREMENT PRIMARY KEY{col_config})")
        self.mydb.commit()
        return tabname

    def getVal(self,table_name,idx,col):
        self.mycursor.execute(f"SELECT {col} FROM {table_name} where id={idx+1}")
        row=self.mycursor.fetchall()
        if len(row)==0:raise KeyError(f"Key:idx-{idx} is not found")
        else:return row[0][0]

    def setVal(self,table_name,idx,col,val):
        if type(val)==str:
            self.mycursor.execute(f"UPDATE {table_name} SET {col}='{val}' WHERE id={idx+1}")
        else:
            self.mycursor.execute(f"UPDATE {table_name} SET {col}={val} WHERE id={idx+1}")
        self.mydb.commit()

    def IncrementBy(self,table_name,idx,col,by):
        self.mycursor.execute(f"UPDATE {table_name} SET {col}={col}+{by} WHERE id={idx+1}")
        self.mydb.commit()

    def Insert(self,table_name,row):
        row_str='0'
        for v in row:
            if type(v)==str:
                row_str+=f", '{v}'"
            else:
                v_reduced='NULL' if np.isnan(v) else v
                row_str+=f", {v_reduced}"
        self.mycursor.execute(f"INSERT INTO {table_name} VALUES ({row_str})")
        self.mydb.commit()

    def getTopicTables(self,):
        self.mycursor.execute("SHOW TABLES")
        return [r[0] for r in self.mycursor if r[0] not in ['subl','publ']]
    
    def Count(self,table_name):
        self.mycursor.execute(f"SELECT count(id) FROM {table_name}")
        res=self.mycursor.fetchall()
        return res[0][0]
    

def env_config():
    config={}
    config['persist']=True if os.environ['PERSIST']=='yes' else False
    return config