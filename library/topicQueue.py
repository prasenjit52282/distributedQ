from collections import deque
from collections import defaultdict

class topicQueue(defaultdict):
    def __init__(self,maxlen=100):
        super().__init__(lambda:deque(maxlen=maxlen))
    
    def push(self,value):
        for k in self.keys():self[k].append(value)