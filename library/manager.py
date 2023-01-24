from .publisher import Publishers
from .subscriber import Subscribers
from .topicq import TopicQueues

class Manager:
    def __init__(self):
        self.tq=TopicQueues()
        self.pubs=Publishers()
        self.subs=Subscribers()
        
    def CreateTopic(self,topic_name):
        if self.tq.is_topic_exist(topic_name):
            return dict(status="failure",message=f"Topic:{topic_name} already exist")
        else:
            self.tq.add_new_topic(topic_name)
            return dict(status="success",message=f"Topic:{topic_name} created successfully")
        
    def ListTopics(self):
        topics=self.tq.get_topic_list()
        if len(topics)==0:
            return dict(status="failure",message=f"No Topic found")
        else:
            return dict(status="success",message=topics)
        
    def RegisterConsumer(self,topic_name):
        if not self.tq.is_topic_exist(topic_name):
            return dict(status="failure",message=f"Topic:{topic_name} does not exist")
        else:
            sub_id=self.subs.add_subscriber()
            last_topic_idx=self.tq.topic_last_idx(topic_name)
            self.subs.reg_subcriber_with_topic(sub_id,topic_name,last_topic_idx)
            return dict(status="success",consumer_id=sub_id)

    def RegisterProducer(self,topic_name):
        if not self.tq.is_topic_exist(topic_name):
            self.tq.add_new_topic(topic_name)
        pub_id=self.pubs.add_publisher()
        self.pubs.reg_publisher_with_topic(pub_id,topic_name)
        return dict(status="success",producer_id=pub_id)


    def Size(self,topic_name,sub_id):
        if not self.subs.is_valid_id(sub_id):
            return dict(status="failure",message=f"Consumer:{sub_id} does not exist")
        if not self.tq.is_topic_exist(topic_name):
            return dict(status="failure",message=f"Topic:{topic_name} does not exist")
        if not self.subs.is_subscriber_reg_with_topic(sub_id,topic_name):
            return dict(status="failure",message=f"Consumer:{sub_id} is not registered with Topic:{topic_name}")
        curr_idx=self.subs.get_curr_idx(sub_id)
        size=self.tq.topic_qsize(topic_name,curr_idx)
        return dict(status="success",size=size)