import numpy as np
from .helper import DataHandler

class Publishers:
    def __init__(self):
        self.publ=self.get_init_pub_list()
        
    def get_init_pub_list(self):
        return DataHandler(columns=['topic'])

    def add_publisher(self):
        pub_id=self.publ.Count
        self.publ.Insert([np.nan])
        return pub_id

    def reg_publisher_with_topic(self,pub_id,topic_name): #id is same is index
        self.publ.Update(pub_id,"topic",topic_name)

    def is_publisher_reg_with_topic(self,pub_id,topic_name):
        return self.publ.GetAT(pub_id,"topic")==topic_name

    def is_valid_id(self,pub_id):
        return 0<=pub_id<self.publ.Count