Note: 
- Ignore any warning for now, for development purpose only
- Warning is important, please do not ignore warning in production


## Install MLflow using Docker

I created a new docker-compose.yaml based on this repo: https://github.com/sachua/mlflow-docker-compose.git

## MLflow UI
Akses MLflow UI di http://localhost:5000/

## Minio
Akses Minio UI di http://localhost:9001/browser/mlflow


## Start tracking model deployment

check current running docker container name
docker ps
get the CONTAINER ID and copy paste in <mycontainer>
docker exec -it <mycontainer> bash

run above command in your local terminal to switch to docker cli


## Run script
in the docker cli, change dir to /opt/mlflow/scripts and you will find the mounted script from your local computer.
run python3 1_example_autolog.py


