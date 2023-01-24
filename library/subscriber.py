import numpy as np
import pandas as pd

class Subscribers:
    def __init__(self):
        self.subl=self.get_init_sub_list()

    def get_init_sub_list(self):
        return pd.DataFrame(columns=['consumed'])

    def add_subscriber(self):
        sub_id=self.subl.shape[0] #index is the sub_id
        self.subl.loc[self.subl.shape[0]]=[0]+([np.nan]*(self.subl.shape[1]-1))
        return sub_id

    def add_topic_name_to_topic_list(self,topic_name):
        self.subl[topic_name]=np.nan

    def get_topic_list(self):
        return list(self.subl.columns[1:])

    def is_topic_exist_in_topic_list(self,topic_name):
        return (topic_name in self.subl.columns[1:])

    def reg_subcriber_with_topic(self,sub_id,topic_name,last_topic_idx): #last_topic_idx=curr idx of messages in topic
        self.subl.loc[sub_id,topic_name]=last_topic_idx

    def is_subscriber_reg_with_topic(self,sub_id,topic_name):
        return (not np.isnan(self.subl.loc[sub_id,topic_name]))

    def topic_consumed_increase_offset(self,sub_id,topic_name): #only when a valid consume has happened
        self.subl.loc[sub_id,topic_name]+=1
        self.subl.loc[sub_id,"consumed"]+=1