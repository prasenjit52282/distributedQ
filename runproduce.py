import time
import random
import argparse
from myqueue import MyProducer,readProduceLog

parser=argparse.ArgumentParser(description='example: python runproduce.py --id 1 --topics T-1 T-2 T-3 --broker 10.110.10.216:5000 --log_loc ./test')

parser.add_argument('--id', type=int, help='id of producer/consumer', required=True)
parser.add_argument('--topics', type=str, nargs='+', help='topics to produce/consume', required=True)
parser.add_argument('--broker', type=str, help='broker address ip:port', required=True)
parser.add_argument('--log_loc', type=str, help='log folder', required=True)

args = parser.parse_args()

def produce(pid=1,topics=['T-1','T-2','T-3'],broker='10.110.10.216:5000',log_loc='./test'):
    producer = MyProducer(
        topics=topics,
        broker=broker)
    try:
        log_gen=readProduceLog(f'{log_loc}/producer_{pid}.txt')
        while producer.can_send():
            for t in topics:
                topic,msg=next(log_gen)
                if t!=topic:raise Exception("log file:incompitable, make sure msg for topics are in order for a perticular time")
                producer.send(topic,msg)
            time.sleep(random.random())
    except StopIteration:pass
    finally:
        producer.stop()

produce(args.id,args.topics,args.broker,args.log_loc)