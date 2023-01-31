# Prerequisites

### 1. Docker: latest [version 20.10.23, build 7155243]

    sudo apt-get update

    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release

    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io

### 2. Docker-compose standalone [version v2.15.1]
    sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
    
    sudo chmod +x /usr/local/bin/docker-compose
    
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose




# Installation Steps

### Deploy broker 
    persistent mode
    └── sudo docker-compose --env-file ./config/.env.persist up -d

    inMemory mode
    └──sudo docker-compose --env-file ./config/.env.inmem up -d

### Restart broker 
    sudo docker-compose restart

### Remove broker
    sudo docker-compose down --rmi all

# Testing

### run a producer instance from log file
    COMMAND
    └──python runproduce.py --id 1 --topics T-1 T-2 T-3 --broker 10.110.10.216:5000 --log_loc ./test

** producer_{id}.txt log file format must be maintained else throws <strong>Exception("log file:incompitable")</strong>

    [ts         msg       parallel    topic]
    ---------------------------------------
    21:52:23	INFO		P1-1		T-1
    21:52:23	INFO		P1-1		T-2
    21:52:23	INFO		P1-1		T-3
    21:52:23	INFO		P1-2		T-1
    21:52:23	INFO		P1-2		T-2
    21:52:23	INFO		P1-2		T-3

### run a consumer instance and store log
    COMMAND
    └──python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker 10.110.10.216:5000 --log_loc ./test

** consumer_{id}.txt stored log file example 

    [ts      msg]
    ---------------------------------------
    T-1     INFO
    T-2     INFO
    T-3     INFO
    T-2     WARN
    T-1     INFO

### run API test cases
    COMMAND
    └──bash testAPI.sh 10.110.10.216 5000

### run 5-producer, 3-consumer setup
Question: Implement 5 Producers and 3 consumers with 3 topics using the library developed in Part-C. Given below is the "topic:producers:consumers" mapping.

+ T1: P1 P2 P3: C1 C2 C3
+ T2: P1 P4 P5: C1 
+ T3: P1 P2: C1 C2 C3

Here, the last point means that P1 and P2 will produce to topic T3;  C1, C2 and C3 will consume from T3.

    [Producers]
    └──python runproduce.py --id 1 --topics T-1 T-2 T-3 --broker 10.110.10.216:5000 --log_loc ./test
    └──python runproduce.py --id 2 --topics T-1 T-3 --broker 10.110.10.216:5000 --log_loc ./test
    └──python runproduce.py --id 3 --topics T-1 --broker 10.110.10.216:5000 --log_loc ./test
    └──python runproduce.py --id 4 --topics T-2 --broker 10.110.10.216:5000 --log_loc ./test
    └──python runproduce.py --id 5 --topics T-2 --broker 10.110.10.216:5000 --log_loc ./test

    [Consumers]
    └──python runconsume.py --id 1 --topics T-1 T-2 T-3 --broker 10.110.10.216:5000 --log_loc ./test
    └──python runconsume.py --id 2 --topics T-1 T-3 --broker 10.110.10.216:5000 --log_loc ./test
    └──python runconsume.py --id 3 --topics T-1 T-3 --broker 10.110.10.216:5000 --log_loc ./test

    Run all commands together
    -------------------------
    + bash test5P3C.sh 10.110.10.216 5000

** Consumer logs are stored at <strong>./test/consumer_{id}.txt</strong> where id = 1,2,3