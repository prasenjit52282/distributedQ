import numpy as np
import pandas as pd

class Subscribers:
    def __init__(self):
        self.subl=self.get_init_sub_list()
        
    def get_init_sub_list(self):
        return pd.DataFrame(columns=['topic','curr_idx'])

    def add_subscriber(self):
        sub_id=self.subl.shape[0] #index is the sub_id
        self.subl.loc[self.subl.shape[0]]=[np.nan,np.nan]
        return sub_id

    def reg_subcriber_with_topic(self,sub_id,topic_name,last_topic_idx): #last_topic_idx=curr idx of msg in topic
        self.subl.loc[sub_id,'topic']=topic_name
        self.subl.loc[sub_id,'curr_idx']=last_topic_idx

    def is_subscriber_reg_with_topic(self,sub_id,topic_name):
        return self.subl.loc[sub_id,"topic"]==topic_name
    
    def topic_consumed_increase_curr_idx(self,sub_id): #only when a valid consume has happened
        self.subl.loc[sub_id,'curr_idx']+=1
        
    def get_curr_idx(self,sub_id):
        return int(self.subl.loc[sub_id,'curr_idx'])

    def is_valid_id(self,sub_id):
        return 0<=sub_id<self.subl.shape[0]