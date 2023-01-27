from .helper import DataHandler
from threading import Semaphore

class TopicQueues:
    def __init__(self):
        self.queues={}
        self.locks={}
        
    def get_empty_topic_log(self):
        return DataHandler(columns=['msg'])

    def add_msg_to_log(self,log_df,msg): #index is the order & time
        log_df.Insert(msg)
        
    def add_new_topic(self,topic_name):
        self.queues[topic_name]=self.get_empty_topic_log()
        self.locks[topic_name]=Semaphore()
        
    def add_msg_for_topic(self,topic_name,msg):
        self.locks[topic_name].acquire()
        self.add_msg_to_log(self.queues[topic_name],msg)
        self.locks[topic_name].release()
        
    def topic_qsize(self,topic_name,curr_idx_in_q):
        return self.queues[topic_name].Count-curr_idx_in_q
        #curr_idx_in_q is where (not read the data yet,already 1 less so no +1) the consumer_id currently in queue
    
    def topic_last_idx(self,topic_name):
        idx=self.queues[topic_name].Count-1
        return 0 if idx<0 else idx

    def get_topic_list(self):
        return list(self.queues.keys())

    def is_topic_exist(self,topic_name):
        return topic_name in self.queues

    def get_msg_for_topic_at_idx(self,topic_name,idx):
        return self.queues[topic_name].GetAT(idx,'msg')