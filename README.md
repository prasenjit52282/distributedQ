# Deploy Broker
    1. Build the image
        * docker build -f Dockerfile -t broker . 

    2. Run the image
        * docker run -d --restart=always --name=broker -p 5000:5000 broker