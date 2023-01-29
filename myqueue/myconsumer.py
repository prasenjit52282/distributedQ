from .api import ApiHandler
from iterators import TimeoutIterator

class MyConsumer:
    def __init__(self,topics,broker,timeout=5):
        self.timeout=timeout
        self.api=ApiHandler(broker)
        self._setup(topics)
        
    def _setup(self,topics):
        self.topics_to_id={}
        for t in topics:
            self.topics_to_id[t]=self.api.reg_consumer(t)
    
    def get_next(self):
        for m in TimeoutIterator(self.consume(),timeout=self.timeout,sentinel=None):
            if m==None:break
            yield m
    
    def consume(self):
        while True:
            for topic,consumer_id in self.topics_to_id.items():
                if self.api.can_get_next(topic,consumer_id):
                    yield self.api.consume(topic,consumer_id)
        
    def stop(self):
        pass