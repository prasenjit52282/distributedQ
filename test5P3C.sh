HOST=$1
PORT=$2

#creating topics
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T1"}' -H "Content-Type: application/json"
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T2"}' -H "Content-Type: application/json"
curl -XPOST "http://${HOST}:${PORT}/topics" -d '{"topic_name": "T3"}' -H "Content-Type: application/json"

#consumers
python runconsume.py --id 1 --topics T1 T2 T3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runconsume.py --id 2 --topics T1 T3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runconsume.py --id 3 --topics T1 T3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
echo "3 consumers are started"

#producers
python runproduce.py --id 1 --topics T1 T2 T3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 2 --topics T1 T3 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 3 --topics T1 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 4 --topics T2 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
python runproduce.py --id 5 --topics T2 --broker  ${HOST}:${PORT} --log_loc ./test/5P3C &
echo "5 producers are started"

wait