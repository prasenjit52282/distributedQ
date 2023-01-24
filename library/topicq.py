import numpy as np
import pandas as pd

class TopicQueues:
    def __init__(self):
        self.queues={}
        
    def get_empty_topic_log(self):
        return pd.DataFrame(columns=['msg'])

    def add_msg_to_log(self,log_df,msg): #index is the order & time
        log_df.loc[log_df.shape[0]]=msg
        
    def add_new_topic(self,topic_name):
        if topic_name not in self.queues:
            self.queues[topic_name]=self.get_empty_topic_log()
        
    def add_msg_for_topic(self,topic_name,msg):
        self.add_msg_to_log(self.queues[topic_name],msg)
        
    def topic_qsize(self,topic_name,curr_idx_in_q):
        return self.queues[topic_name].shape[0]-curr_idx_in_q
        #curr_idx_in_q is where (not read the data yet,already 1 less so no +1) the consumer_id currently in queue
    
    def topic_last_idx(self,topic_name):
        idx=self.queues[topic_name].shape[0]-1
        return 0 if idx<0 else idx