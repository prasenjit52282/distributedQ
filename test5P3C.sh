HOST=$1
PORT=$2

#creating topics
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T-1"}' -H "Content-Type: application/json"
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T-2"}' -H "Content-Type: application/json"
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T-3"}' -H "Content-Type: application/json"


#producers
python runproduce.py --id 1 --topics T-1 T-2 T-3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 2 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 3 --topics T-1 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 4 --topics T-2 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 5 --topics T-2 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
echo "5 producers are started"

#consumers
python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runconsume.py --id 2 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runconsume.py --id 3 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
echo "3 consumers are started"

wait