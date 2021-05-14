# Guidelines for installing a container with a VERIFACE face recognition system on a server machine


## Requirements 

Installed docker, docker-compose

This module compares two faces with each other


## Installation 
* Put face detection models in folder `dengi-group/server/models/face_detection/`
* Put checkpoints in folder `dengi-group/server/models/face_recognition/`
* Put liveness model in folder `dengi-group/server/liveness-model/`

Finally you need to run `docker-compose up` command.

Installation complete
#### Open new docker terminal and create table logs by following commands
In new terminal run 
```docker exec -ti dengi-group_db_1 psql -U postgres```
* Create table logs ```CREATE TABLE logs(id SERIAL PRIMARY KEY,full_recognition_time VARCHAR, doc VARCHAR, photo VARCHAR, score VARCHAR, cos_distance VARCHAR, boundingbox_doc VARCHAR, boundingbox_photo VARCHAR);```

## Test POST

To compare two images just send POST request like example bellow:

```
curl -X POST -F "photo=@<path to the photo from WebCamera>" -F "doc=@<path to the photo from the document>" localhost:5000/

```

##View logs
* In terminal where table logs was created run ```select * from logs;```