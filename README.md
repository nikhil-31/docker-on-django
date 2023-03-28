
## Docker on django

### Overview

### Technologies used
- docker
- django


## running elastic search

- Running kibana
```
docker run --name kib-01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.6.2
```

- Running elastic 
```
docker run --name es-node01 --net elastic -p 9200:9200 -p 9300:9300 -t docker.elastic.co/elasticsearch/elasticsearch:8.6.2
```