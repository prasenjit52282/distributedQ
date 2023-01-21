import shelve
from .topicQueue import topicQueue

class messageQueue:
    def __init__(self,topicQmaxlen=100,persistent=False,save_path="./logs"):
        self.topicQmaxlen=topicQmaxlen
        if persistent:self.buf=shelve.open(save_path)
        else:self.buf={}
        self.setupBuf()

    def setupBuf(self):
        if "__MQ_topic_to_producer" not in self.buf:
            self.buf["__MQ_topic_to_producer"]={}
        if "__MQ_info" not in self.buf:
            self.buf["__MQ_info"]=dict(producer_count=0,consumer_count=0)

    def getProducerID(self):
        id=self.buf["__MQ_info"]["producer_count"]
        self.buf["__MQ_info"]["producer_count"]+=1
        return id
    
    def getConsumerID(self):
        id=self.buf["__MQ_info"]["consumer_count"]
        self.buf["__MQ_info"]["consumer_count"]+=1
        return id
    
    def createTopic(self,topic):
        if topic not in self.buf:self.buf[topic]=topicQueue(maxlen=self.topicQmaxlen)
        else:raise Exception(f"Topic: {topic} already exist")

    def listTopics(self):
        return list(self.buf.keys())
    
    def registerConsumer(self,topic):
        if topic not in self.buf:raise Exception(f"Topic: {topic} does not exist")
        else:
            id=self.getConsumerID()
            self.buf[topic][id]
            return id
        
    def registerProducer(self,topic):
        if topic in self.buf["__MQ_topic_to_producer"]:
            raise Exception("A producer is already using this topic to publish")
        id=self.getProducerID()
        if topic not in self.buf:
            self.createTopic(topic)
        self.buf["__MQ_topic_to_producer"][topic]=id
        return id

    def enqueue(self,topic,producer_id,message):
        if topic not in self.buf:
            raise Exception(f"Topic: {topic} does not exist")
        if self.buf["__MQ_topic_to_producer"][topic]!=producer_id:
            raise Exception(f"Producer: {producer_id} is not registered with topic {topic}")
        self.buf[topic].push(message)