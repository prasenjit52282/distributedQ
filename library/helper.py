import pandas as pd

class DataHandler:
    def __init__(self,columns=None,is_SQL=False,cred_SQL=None,db=None,table_name=None):
        self.columns=columns
        self.is_SQL=is_SQL
        self.cred_SQL=cred_SQL
        self.db=db;self.table_name=table_name
        self._setup()

    def _setup(self):
        if not self.is_SQL:
            self.table=pd.DataFrame(columns=self.columns)
        else:
            #setup sql cursor
            pass
    
    @property
    def Count(self):
        if not self.is_SQL:
            return self.table.shape[0]
        else:
            #count entries and return
            return 0

    def Insert(self,row):
        if not self.is_SQL:
            self.table.loc[self.table.shape[0]]=row
        else:
            #count entries and return
            pass

    def Update(self,idx,col,val):
        if not self.is_SQL:
            self.table.loc[idx,col]=val
        else:
            #count entries and return
            pass

    def GetAT(self,idx,col):
        if not self.is_SQL:
            return self.table.loc[idx,col]
        else:
            #count entries and return
            return 0