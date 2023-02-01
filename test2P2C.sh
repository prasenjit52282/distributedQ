HOST=$1
PORT=$2

#creating topics
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T1"}' -H "Content-Type: application/json"
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T2"}' -H "Content-Type: application/json"

#consumers
python runconsume.py --id 1 --topics T1 T2 --broker  ${HOST}:${PORT} --log_loc ./test/2P2C &
python runconsume.py --id 2 --topics T1 T2 --broker  ${HOST}:${PORT} --log_loc ./test/2P2C &
echo "2 consumers are started"

#producers
python runproduce.py --id 1 --topics T1 T2 --broker  ${HOST}:${PORT} --log_loc ./test/2P2C &
python runproduce.py --id 2 --topics T1 T2 --broker  ${HOST}:${PORT} --log_loc ./test/2P2C &
echo "2 producers are started"

wait