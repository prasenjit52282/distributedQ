HOST=$1
PORT=$2


#producers
python runproduce.py --id 1 --topics T-1 T-2 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runproduce.py --id 2 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runproduce.py --id 3 --topics T-1 --broker  ${HOST}:${PORT} --log_loc ./test &
python runproduce.py --id 4 --topics T-2 --broker  ${HOST}:${PORT} --log_loc ./test &
python runproduce.py --id 5 --topics T-2 --broker  ${HOST}:${PORT} --log_loc ./test &
echo "5 producers are started"

sleep 1 #sleep for 1 sec

#consumers
python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 2 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 3 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
echo "3 consumers are started"

wait