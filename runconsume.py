import argparse
from myqueue import MyConsumer,writeComsumeLog

parser=argparse.ArgumentParser(description='example: python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker 10.110.10.216:5000 --log_loc ./test')

parser.add_argument('--id', type=int, help='id of producer/consumer', required=True)
parser.add_argument('--topics', type=str, nargs='+', help='topics to produce/consume', required=True)
parser.add_argument('--broker', type=str, help='broker address ip:port', required=True)
parser.add_argument('--log_loc', type=str, help='log folder', required=True)

args = parser.parse_args()

def consume(cid=1,topics=['T-1','T-2','T-3'],broker='10.110.10.216:5000',log_loc='./test'):
    consumer = MyConsumer(
        topics=topics,
        broker=broker)
    try:
        writer=writeComsumeLog(f'{log_loc}/consumer_{cid}.txt')
        for msg in consumer.get_next():
            writer.writeline(f"{msg.topic}     {msg.message}")
    except:writer.close()
    finally:
        consumer.stop()

consume(args.id,args.topics,args.broker,args.log_loc)