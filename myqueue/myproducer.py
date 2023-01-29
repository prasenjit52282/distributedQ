from .api import ApiHandler

class MyProducer:
    def __init__(self,topics,broker):
        self.api=ApiHandler(broker)
        self._setup(topics)
        
    def _setup(self,topics):
        self.topics_to_id={}
        for t in topics:
            self.topics_to_id[t]=self.api.reg_producer(t)
            
    def can_send(self):
        return self.api.can_send()
    
    def send(self,topic,msg):
        self.api.produce(topic,self.topics_to_id[topic],msg)
        
    def stop(self):
        pass