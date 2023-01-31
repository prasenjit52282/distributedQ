HOST=$1
PORT=$2


#producers
python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 2 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 3 --topics T-1 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 4 --topics T-2 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 5 --topics T-2 --broker  ${HOST}:${PORT} --log_loc ./test &

sleep 1 #sleep for 5 sec

#consumers
python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 2 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &
python runconsume.py --id 3 --topics T-1 T-3 --broker  ${HOST}:${PORT} --log_loc ./test &

wait