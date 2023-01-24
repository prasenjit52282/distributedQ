import numpy as np
import pandas as pd

class Publishers:
    def __init__(self):
        self.publ=self.get_init_pub_list()
        
    def get_init_pub_list(self):
        return pd.DataFrame(columns=['topic'])

    def add_publisher(self):
        pub_id=self.publ.shape[0] #index is the pub_id
        self.publ.loc[self.publ.shape[0],"topic"]=np.nan
        return pub_id

    def reg_publisher_with_topic(self,pub_id,topic_name): #id is same is index
        self.publ.loc[pub_id,"topic"]=topic_name

    def is_publisher_reg_with_topic(self,pub_id,topic_name):
        return self.publ.loc[pub_id,"topic"]==topic_name